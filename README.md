# Project Bidimensional Layout
## Overview
The Bidimensional Layout Project focuses on positioning multiple buildings within a rectangular site, adhering to distance constraints among them and optimizing objectives such as:

Minimizing total distance between related buildings,
Maximizing the efficient usage of the site’s area,
Avoiding overlapping among buildings,
Respecting minimum and maximum separation distances for paths.

Key modules include:

Data loading: Input data structures (buildings, paths, objectives).

Initial solution: A heuristic approach to generate a basic layout.

Improved solution: Additional heuristics to refine the initial arrangement (e.g., rotating buildings, repositioning them with respect to distance constraints).

Visualization: A module to display the resulting layout in 2D.

JSON export: Utility to store final layouts or solutions in a JSON format.

## Project Architecture
1. Data
Defines core classes like Building, Path, Objective, and the loader for reading JSON input.
2. Optimizer
Contains the logic to generate an initial layout (in initial_solution) and improved layouts (in improved_solutions).
3. Visualization
Provides functions to plot the 2D distribution of buildings.
4. Main
A script (main.py) that orchestrates data loading, solution generation, and visualization.

## Installation and Requirements
1. WSL and conda (optional, but recommended if you are on Windows).

2. Python 3.9+.

3. Necessary Python libraries. For instance, you can install them via conda or pip:

        conda install numpy matplotlib

    or

        pip install numpy matplotlib

4. (Optional) Git and VS Code if you want to replicate the same development environment.

### Creating a Conda Environment

    conda create -n layout_env python=3.9
    conda activate layout_env

## Usage
The project provides various scripts and functions inside the src/ folder. A typical workflow might be:

### Generating the Initial Solution

In src/main.py, the code loads a JSON file (e.g., input_instance.json) and calls generate_initial_solution. A simple command-line example:

    python src/main.py

This will print, in the terminal:

-The total used area,

-The total distance for linked buildings,

-The utilization factor (ratio of used area to the total site area),

It can also open a matplotlib window to visualize the layout.

### Generating an Improved Solution

Inside src/optimizer/improved_solutions/, the function first_heuristic_solution refines the initial layout:

      from optimizer.improved_solutions.improved_solution import first_heuristic_solution

      improved_sol = first_heuristic_solution(layout_data, initial_sol)

It repositions buildings while respecting min/max distances defined by their Path connections, optionally rotating buildings, etc.

### Visualization
You can display both the initial and improved layouts using Matplotlib:

src/visualization/initial_layout.py for the initial solution,

src/visualization/improved_layout.py for the improved solution.

For example:

    from visualization.initial_layout import plot_initial_layout
    plot_initial_layout(initial_solution, layout_data)

And similarly:

    from visualization.improved_layout import plot_improved_layout
    plot_improved_layout(improved_solution, layout_data)

Each building is represented as a rectangle labeled with its name and ID.

### Exporting to JSON

A utility (for instance, save_solution_to_json in src/optimizer/improved_solutions/save_solution.py) can write a final arrangement to a JSON file of this form:

      {
        "arrangement_id": 1,
        "buildings": [
          {"name": "Building 1", "location": [x, y], "dimensions": [2800, 3300]},
          ...
        ],
        "paths": [
          {"name": "Path 1", "length": 50, "connected_buildings": ["Building 1", "Building 2"]},
          ...
        ],
        "total_area": 150000,
        "objectives": {"objective_1": 200, "objective_2": 150000}
      }

This file captures the final layout’s key parameters for further reference or analysis.

## Folder Structure

    bidimensional_layout/
    ├── data/
    │   └── input_instance.json         # Example JSON input
    ├── src/
    │   ├── __init__.py
    │   ├── data/
    │   │   ├── __init__.py
    │   │   ├── model.py                # Building, Path, Objective, LayoutData classes
    │   │   └── loader.py               # Data loading & parsing logic
    │   ├── optimizer/
    │   │   ├── __init__.py
    │   │   ├── initial_solution/
    │   │   │   ├── __init__.py
    │   │   │   └── initial_solution.py # Logic for the initial layout
    │   │   └── improved_solutions/
    │   │       ├── __init__.py
    │   │       ├── improved_solution.py # Improves the initial layout with heuristics
    │   │       └── save_solution.py     # (Optional) Exports a layout to JSON
    │   ├── visualization/
    │   │   ├── __init__.py
    │   │   ├── initial_layout.py       # Visualize the initial layout
    │   │   └── improved_layout.py      # Visualize the improved layout
    │   └── main.py                     # Entry point for the project
    ├── .gitignore
    ├── README.md                       # This file
    ├── environment.yml (or requirements.txt)
    └── ...

## Contact
For more information, suggestions, or bug reports, please contact:

Name: Nicolas Clavijo-Buritica
Email: nicolasclbr@gmail.com
GitHub: github.com/nicolasclbr
