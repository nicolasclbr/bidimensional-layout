from data.loader import load_data
from optimizer.initial_solution.initial_solution import generate_initial_solution
from visualization.initial_layout import plot_initial_layout

def main(json_path: str):
    layout_data = load_data(json_path)
    result = generate_initial_solution(layout_data)
    
    print(f"The aggregate area of all buildings is: {layout_data.site_area/4}")
    print(f"The area assigned for the layout is: {layout_data.site_area}")
    print("Buildings:")
    for b in layout_data.buildings:
        print(f"  {b.id} - {b.name}, {b.building_type}, {b.dimensions}")

    print("Initial solution metrics:")
    print(f"  - used_area: {result['used_area']}")
    print(f"  - free_area: {result['free_area']}")
    print(f"  - utilization_factor: {result['utilization_factor']}")
    print(f"  - total_distance_paths: {result['total_distance_paths']}")
    
    print("Distance Matrix:")
    for row in result['distance_matrix']:
        print(row)
    
    print("Positions:")
    for b_id, (x, y) in result['positions'].items():
        print(f"  Building {b_id} -> x={x}, y={y}")

    plot_initial_layout(result, layout_data)


if __name__ == "__main__":
    main("src/data/input_instance.json")