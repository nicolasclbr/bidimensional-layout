import json
from typing import Union
from pathlib import Path

from .model import Building, Path as LayoutPath, Objective, LayoutData



def load_data(json_path: Union[str, Path]) -> LayoutData:

    """
    The loader is fed from the JSON file and returns a LayoutData object 
    with the lists of buildings, roads, objectives, and site_area. Besides, an unique 'id' 
    is assigned to each building.
    """

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    #parsing buildings
    buildings_by_name = {}
    buildings_list = data.get("buildings", [])

    buildings = []
    for i, b in enumerate(buildings_list, start=1):
        building = Building(
            id=i,
            name=b["name"],
            building_type=b["type"],
            dimensions=tuple(b["dimensions"])
        )
        buildings.append(building)
        buildings_by_name[building.name] = building
    
    #parsing paths
    paths = []
    paths_list = data.get("paths", [])
    for p in paths_list:
        building_1 = buildings_by_name[p["between"][0]]
        building_2 = buildings_by_name[p["between"][1]]

        path = LayoutPath(
            name=p["name"],
            between=(building_1, building_2),
            width=p["width"],
            min_length=p["min_length"],
            max_length=p["max_length"],
            path_type=p["type"]
        )
        paths.append(path)

    #parsing objectives
    objectives = []
    objectives_list = data.get("objectives", [])
    for o in objectives_list:
        objective = Objective(
            name=o["name"],
            description=o["desc"]
        )
        objectives.append(objective)

    site_area = data.get("site_area", None)
    if site_area is None:
        sum_building_area = 0.0
        for b in buildings:
            w, h = b.dimensions
            sum_building_area += (w * h)
        site_area = sum_building_area * 4


    #final object
    layout_data = LayoutData(
        buildings=buildings,
        paths=paths,
        objectives=objectives,
        site_area=site_area
    )
    return layout_data
