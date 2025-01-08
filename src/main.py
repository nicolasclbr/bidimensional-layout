from data.loader import load_data
from optimizer.initial_solution.initial_solution import generate_initial_solution
from optimizer.improved_solutions.improved_solution import first_heuristic_solution
from visualization.initial_layout import plot_initial_layout
from visualization.improved_layout import plot_improved_layout
from optimizer.improved_solutions.save_solution import save_solution_to_json

def main(json_path: str):
    layout_data = load_data(json_path)
    initial_sol = generate_initial_solution(layout_data)
    
    print(f"The aggregate area of all buildings is: {layout_data.site_area/4}")
    print(f"The area assigned for the layout is: {layout_data.site_area}")
    print("Buildings:")
    for b in layout_data.buildings:
        print(f"  {b.id} - {b.name}, {b.building_type}, {b.dimensions}")

    print("Initial solution metrics:")
    print(f"  - used_area: {initial_sol['used_area']}")
    print(f"  - free_area: {initial_sol['free_area']}")
    print(f"  - utilization_factor: {initial_sol['utilization_factor']}")
    print(f"  - total_distance_paths: {initial_sol['total_distance_paths']}")
    
    print("Distance Matrix:")
    for row in initial_sol['distance_matrix']:
        print(row)
    
    print("Positions:")
    for b_id, (x, y) in initial_sol['positions'].items():
        print(f"  Building {b_id} -> x={x}, y={y}")

    plot_initial_layout(initial_sol, layout_data)

    improved_sol = first_heuristic_solution(layout_data, initial_sol)

    print("Improved solution metrics:")
    print(f"  - used_area: {improved_sol['used_area']}")
    print(f"  - free_area: {improved_sol['free_area']}")
    print(f"  - utilization_factor: {improved_sol['utilization_factor']}")
    print(f"  - total_distance_paths: {improved_sol['total_distance_paths']}")

    print("Distance Matrix (improved):")
    for row in improved_sol['distance_matrix']:
        print(row)
    
    print("Positions:")
    for b_id, (x, y) in improved_sol['positions'].items():
        print(f"  Building {b_id} -> x={x}, y={y}")


    plot_improved_layout(improved_sol, layout_data)

    save_solution_to_json(improved_sol, layout_data, arrangement_id=2, filename="improved_solution.json")


if __name__ == "__main__":
    main("src/data/input_instance.json")