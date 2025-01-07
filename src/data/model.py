from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Building:
    id: int
    name: str
    building_type: str
    dimensions: Tuple[float, float]

@dataclass
class Path:
    name: str
    between: Tuple[Building, Building]
    width: float
    min_length: float
    max_length: float
    path_type: str

@dataclass
class Objective:
    name: str
    description: str

@dataclass
class LayoutData:
    buildings: List[Building]
    paths: List[Path]
    objectives: List[Objective]

