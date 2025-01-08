import math
import matplotlib.pyplot as plt
from data.model import LayoutData

def plot_improved_layout(solution: dict, layout_data: LayoutData):
    """
    This function draws the 'site_area' and the improved layout for the arrangement of the buildings.
    """
    site_area = layout_data.site_area
    side = math.sqrt(site_area)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title("Improved Layout")

    # Drawing the total area and buildings
    area_patch = plt.Rectangle((0, 0), side, side, fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(area_patch)

    for b in layout_data.buildings:
        b_id = b.id
        w, h = b.dimensions
        if b_id not in solution["positions"]:
            continue
        x, y = solution["positions"][b_id]

        rect = plt.Rectangle((x, y), w, h, alpha=0.5, edgecolor='blue', facecolor='blue')
        ax.add_patch(rect)

        # Assign label and id to the building
        center_x = x + w/2
        center_y = y + h/2
        ax.text(center_x, center_y, f"{b.name}\nID: {b_id}", 
                ha='center', va='center', color='white', fontsize=8)

    ax.set_xlim(0, side * 1.1)
    ax.set_ylim(0, side * 1.1)
    ax.set_aspect('equal', 'box')
    plt.show()