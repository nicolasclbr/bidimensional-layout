import math
import matplotlib.pyplot as plt
from data.model import LayoutData

def plot_initial_layout(solution: dict, layout_data: LayoutData):
    """
    This function plots the initial layout of the buildings
    """
    site_area = layout_data.site_area
    side = math.sqrt(site_area)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title("Initial Layout")

    # Obtaining the global area
    area_patch = plt.Rectangle((0, 0), side, side, 
                               fill=False, edgecolor='red', linewidth=2, label='site_area')
    ax.add_patch(area_patch)

    # Plotting buildings
    for building in layout_data.buildings:
        b_id = building.id
        w, h = building.dimensions
        
        # Obtaining position (x, y)
        if b_id in solution["positions"]:
            x, y = solution["positions"][b_id]
        else:
            print(f"Warning: No position found for building ID={b_id}")
            continue

        # Drawing the building as a rectangle
        building_patch = plt.Rectangle(
            (x, y), w, h,
            fill=True, alpha=0.5, edgecolor='blue', facecolor='blue'
        )
        ax.add_patch(building_patch)

        # Labeling the building
        center_x = x + w/2
        center_y = y + h/2
        label = f"{building.name}\nID: {b_id}"
        ax.text(center_x, center_y, label,
                ha='center', va='center', fontsize=8, color='white')

    # Setting the plot limits    
    ax.set_xlim(0, side * 1.1)
    ax.set_ylim(0, side * 1.1)
    ax.set_aspect('equal','box')

    # Displaying the plot
    ax.legend()
    plt.show()