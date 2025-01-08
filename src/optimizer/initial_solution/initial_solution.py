import math
from typing import Dict, Any
from data.model import LayoutData, Building

def generate_initial_solution(layout_data: LayoutData) -> Dict[str, Any]:
    """
    Generate an initial solution by placing the building with the largest area 
    in the lower left corner (coordinate (0,0)) 
    """
    # Sort buildings by area
    buildings = layout_data.buildings[:]
    buildings.sort(key=lambda b: b.dimensions[0] * b.dimensions[1], reverse=True)

    # Biggest building is placed in origin
    current_x = 0.0
    current_y = 0.0

    positions = {}

    for i, b in enumerate(buildings):
        w, h = b.dimensions
        # Assigning origin
        positions[b.id] = (current_x, current_y)
        
        if i == 0:
            current_x += w
        else:
            # adjacent buildings in x axis
            positions[b.id] = (current_x, 0.0)
            current_x += w

    # Calculate distance matrix
    n_buildings = len(buildings)
    distance_matrix = [[0.0 for _ in range(n_buildings)] for _ in range(n_buildings)]
    
    for i in range(n_buildings):
        bi = buildings[i]
        (xi, yi) = positions[bi.id]
        wi, hi = bi.dimensions
        
        # Center points i
        center_i = (xi + wi/2, yi + hi/2)
        
        for j in range(n_buildings):
            if i == j:
                distance_matrix[i][j] = 0.0
                continue
            bj = buildings[j]
            (xj, yj) = positions[bj.id]
            wj, hj = bj.dimensions
            
            # Center points j
            center_j = (xj + wj/2, yj + hj/2)
            
            # Distances and matrix generation
            dx = center_i[0] - center_j[0]
            dy = center_i[1] - center_j[1]
            distance_matrix[i][j] = math.hypot(dx, dy)
    
    # Distances for paths
    total_distance_paths = 0.0
    for path in layout_data.paths:
        # finding index i, j in list 'buildings'
        b1 = path.between[0]  # building object
        b2 = path.between[1]
        
        # Finding the connected buildings in distance matrix
        i1 = buildings.index(b1)
        i2 = buildings.index(b2)
        total_distance_paths += distance_matrix[i1][i2]

    # Used area calculation
    used_area = sum([b.dimensions[0] * b.dimensions[1] for b in buildings])

    # Free area calculation
    free_area = layout_data.site_area - used_area if layout_data.site_area > 0 else 0

    # Utilization factor calculation
    utilization_factor = used_area / layout_data.site_area if layout_data.site_area else 0

    return {
        "positions": positions, 
        "distance_matrix": distance_matrix,
        "total_distance_paths": total_distance_paths,
        "used_area": used_area,
        "free_area": free_area,
        "utilization_factor": utilization_factor
    }

