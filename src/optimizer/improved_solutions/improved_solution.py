import math
from typing import Dict, Any
from data.model import LayoutData, Building, Path

def first_heuristic_solution(layout_data: LayoutData, initial_solution: Dict[str, Any]) -> Dict[str, Any]:
    """
    This heuristic sets the location of the largest building at (0,0) 
    and locates its partner to its right side or above, leaving room for the path. 
    It then locates the other buildings avoiding overlap.
    """
    # Identify the largest building based on initial solution
    buildings = layout_data.buildings[:]
    buildings.sort(key=lambda b: b.dimensions[0] * b.dimensions[1], reverse=True)
    biggest_building = buildings[0]
    biggest_b_id = biggest_building.id

    improved_positions = dict(initial_solution["positions"]) 

    # Identify which Paths involve the largest building
    paths_to_biggest = []
    for p in layout_data.paths:
        b1, b2 = p.between
        if b1 == biggest_building or b2 == biggest_building:
            paths_to_biggest.append(p)
    
    if not paths_to_biggest:
        return initial_solution
    
    main_path = paths_to_biggest[0]
    # Identify the building couple (based on 'between')
    other_building = main_path.between[0] if main_path.between[1] == biggest_building else main_path.between[1]

    # Find the min_length and max_length
    min_dist = main_path.min_length
    max_dist = main_path.max_length

    # Relocate the other building (couple of biggest_building)
    (big_w, big_h) = biggest_building.dimensions
    (big_x, big_y) = improved_positions[biggest_b_id]
    (ob_w, ob_h) = other_building.dimensions
    
    new_y = big_y + big_h + min_dist
    new_x = big_x

    improved_positions[other_building.id] = (new_x, new_y)

    # Relocate remaining buildings

    # Recalculate metrics
    improved_distance_matrix = _recompute_distances(buildings, improved_positions)
    improved_total_distance_paths = _compute_total_path_distance(buildings, improved_distance_matrix, layout_data.paths)
    used_area = sum(b.dimensions[0] * b.dimensions[1] for b in buildings)
    free_area = layout_data.site_area - used_area if layout_data.site_area > 0 else 0
    utilization_factor = used_area / layout_data.site_area if layout_data.site_area else 0

    improved_solution = {
        "positions": improved_positions,
        "distance_matrix": improved_distance_matrix,
        "total_distance_paths": improved_total_distance_paths,
        "used_area": used_area,
        "free_area": free_area,
        "utilization_factor": utilization_factor
    }

    return improved_solution

def _recompute_distances(buildings, positions):
    """
    This function recalculates the matrix of distances between geometrical centers
    """
    n_buildings = len(buildings)
    distance_matrix = [[0.0 for _ in range(n_buildings)] for _ in range(n_buildings)]
    
    for i in range(n_buildings):
        bi = buildings[i]
        (xi, yi) = positions[bi.id]
        wi, hi = bi.dimensions
        
        center_i = (xi + wi / 2, yi + hi / 2)
        
        for j in range(n_buildings):
            if i == j:
                distance_matrix[i][j] = 0.0
                continue
            bj = buildings[j]
            (xj, yj) = positions[bj.id]
            wj, hj = bj.dimensions
            
            center_j = (xj + wj / 2, yj + hj / 2)
            
            dx = center_i[0] - center_j[0]
            dy = center_i[1] - center_j[1]
            distance_matrix[i][j] = math.hypot(dx, dy)
    
    return distance_matrix

def _compute_total_path_distance(buildings, distance_matrix, paths):
    """
    This function recalculates the total distance for buildings connected by 'Path'.
    """
    total_distance = 0.0
    for path in paths:
        b1 = path.between[0]
        b2 = path.between[1]
        i1 = buildings.index(b1)
        i2 = buildings.index(b2)
        total_distance += distance_matrix[i1][i2]
    
    return total_distance