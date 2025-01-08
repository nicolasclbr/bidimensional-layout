import json
from typing import Dict, Any
from data.model import LayoutData

def save_solution_to_json(
    solution: Dict[str, Any],
    layout_data: LayoutData,
    arrangement_id: int,
    filename: str
) -> None:
    """
    Generates a JSON file with the solution information.
    """
    # buildings array
    buildings_data = []
    for b in layout_data.buildings:
        x, y = solution["positions"][b.id]
        buildings_data.append({
            "name": b.name,
            "location": [x, y],
            "dimensions": list(b.dimensions)
        })

    # paths array calculated from the matrix
    paths_data = []
    b_id_to_index = {b.id: i for i, b in enumerate(layout_data.buildings)}

    for p in layout_data.paths:
        b1, b2 = p.between
        idx1 = b_id_to_index[b1.id]
        idx2 = b_id_to_index[b2.id]
        dist = solution["distance_matrix"][idx1][idx2]  # dist between building b1 and b2

        paths_data.append({
            "name": p.name,
            "length": dist,
            "connected_buildings": [b1.name, b2.name]
        })
    
    #  - objective_1 -> sum of path lengths
    #  - objective_2 -> free area
    objectives_data = {
        "objective_1": solution["total_distance_paths"],  
        "objective_2": solution["free_area"]
    }
    
    result = {
        "arrangement_id": arrangement_id,
        "buildings": buildings_data,
        "paths": paths_data,
        "total_area": layout_data.site_area,
        "objectives": objectives_data
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)