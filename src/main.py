from data.loader import load_data

def main(json_path: str):
    layout_data = load_data(json_path)
    
    print(f"The aggregate area of all buildings is: {layout_data.site_area/4}")
    print(f"The area assigned for the layout is: {layout_data.site_area}")
    print("Buildings:")
    for b in layout_data.buildings:
        print(f"  {b.id} - {b.name}, {b.building_type}, {b.dimensions}")


if __name__ == "__main__":
    main("src/data/input_instance.json")