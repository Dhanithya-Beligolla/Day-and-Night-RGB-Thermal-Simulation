import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle, Arc

def normalize_color(color):
    """Convert RGB values from the 0-255 range to the 0-1 range for plotting."""
    return tuple(c / 255.0 for c in color)

def plot_map_rgb(map_rgb_view, map_blocks, hour, title="RGB Map View", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 10))

    # Brightness factor simulates day/night effect, higher during the day and lower at night
    brightness_factor = np.sin(np.pi * hour / 24)

    # Predefined colors for common item types on the map
    default_colors = {
        "Tree": (0, 100, 0),     # Dark Green for trees
        "House": (139, 69, 19),  # Brown for houses
        "Road": (128, 128, 128), # Gray for roads
        "Pond": (0, 0, 255),     # Blue for ponds
        "Animal": (255, 0, 0),   # Red for animals
    }

    # Set a light green background to represent grass or open land
    ax.set_facecolor(normalize_color((144, 238, 144)))

    # Iterate over each block and plot its items based on their type
    for i, row in enumerate(map_blocks):
        for j, block in enumerate(row):
            for item in block.items:
                # Determine the item's base color from predefined mappings or default to white
                base_color = np.array(default_colors.get(item.name, [255, 255, 255])) / 255.0

                # Adjust brightness based on the time of day
                adjusted_color = base_color * brightness_factor

                # Ensure color values remain within the valid range (0-1)
                adjusted_color = np.clip(adjusted_color, 0, 1)

                # Plot different shapes based on the item type (e.g., trees as circles, houses as rectangles)
                if item.name == "Tree":
                    circle = Circle((j + 0.5, map_rgb_view.shape[0] - i - 0.5), radius=item.radius, color=adjusted_color)
                    ax.add_patch(circle)
                elif item.name == "House":
                    rect = Rectangle((j, map_rgb_view.shape[0] - i - 1), item.width, item.length, color=adjusted_color)
                    ax.add_patch(rect)
                elif item.name == "Road":
                    rect = Rectangle((j - 0.5, map_rgb_view.shape[0] - i - 1.5), item.width, 1, color=adjusted_color)
                    ax.add_patch(rect)
                elif item.name == "Pond":
                    circle = Circle((j + 0.5, map_rgb_view.shape[0] - i - 0.5), radius=item.radius, color=normalize_color((0, 0, 255)))
                    ax.add_patch(circle)
                elif item.name == "Animal":
                    circle = Circle((j + 0.5, map_rgb_view.shape[0] - i - 0.5), radius=0.15, color=adjusted_color)
                    ax.add_patch(circle)

    # Set plot title and axis limits to match the map size
    ax.set_title(title)
    ax.set_xticks(np.arange(0, map_rgb_view.shape[1], step=5))
    ax.set_yticks(np.arange(0, map_rgb_view.shape[0], step=5))
    ax.set_xlim(0, map_rgb_view.shape[1])
    ax.set_ylim(0, map_rgb_view.shape[0])
    ax.set_aspect('equal')
    ax.grid(False)


def plot_map_thermal(map_thermal_view, map_blocks, hour, title="Thermal Map View", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 10))

    thermal_cmap = plt.get_cmap('hot')  # Use a heatmap color scheme for thermal views

    # Contrast factor simulates the effect of day/night on the thermal map
    contrast_factor = np.sin(np.pi * hour / 24)

    # Predefined colors for thermal views of different item types
    default_colors = {
        "Tree": (255, 165, 0),  # Orange
        "House": (255, 255, 0),  # Yellow
        "Animal": (255, 0, 0),   # Red
        "Pond": (0, 0, 255),     # Blue
        "Road": (128, 128, 128),  # Gray
    }

    # Display the thermal data as an image
    img = ax.imshow(map_thermal_view, cmap=thermal_cmap, extent=[0, map_thermal_view.shape[1], 0, map_thermal_view.shape[0]], origin='upper')

    # Plot different items with their respective thermal colors
    for i, row in enumerate(map_blocks):
        for j, block in enumerate(row):
            for item in block.items:
                # Get the item's base color from predefined mappings or default to white
                base_color = np.array(default_colors.get(item.name, [255, 255, 255])) / 255.0

                # Adjust brightness based on the contrast factor
                adjusted_color = base_color * contrast_factor

                # Ensure color values remain within the valid range (0-1)
                adjusted_color = np.clip(adjusted_color, 0, 1)

                # Override certain item types like water and roads to keep their fixed colors
                if item.name == "Pond":
                    color = normalize_color((0, 0, 255))  # Always blue for water
                elif item.name == "Road":
                    color = normalize_color((128, 128, 128))  # Always gray for roads
                else:
                    color = adjusted_color  # Use adjusted color for other items

                # Plot different shapes based on the item type
                if item.name == "Tree":
                    circle = Circle((j + 0.5, map_thermal_view.shape[0] - i - 0.5), radius=item.radius, color=color)
                    ax.add_patch(circle)
                elif item.name == "House":
                    rect = Rectangle((j, map_thermal_view.shape[0] - i - 1), item.width, item.length, color=color)
                    ax.add_patch(rect)
                elif item.name == "Road":
                    rect = Rectangle((j - 0.5, map_thermal_view.shape[0] - i - 1.5), item.width, 1, color=color, alpha=0.8)
                    ax.add_patch(rect)
                elif item.name == "Pond":
                    circle = Circle((j + 0.5, map_thermal_view.shape[0] - i - 0.5), radius=item.radius, color=color)
                    ax.add_patch(circle)
                elif item.name == "Animal":
                    circle = Circle((j + 0.5, map_thermal_view.shape[0] - i - 0.5), radius=0.15, color=color)
                    ax.add_patch(circle)

    # Configure the axis limits and grid settings
    ax.set_xticks(np.arange(0, map_thermal_view.shape[1], step=5))
    ax.set_yticks(np.arange(0, map_thermal_view.shape[0], step=5))
    ax.set_xlim(0, map_thermal_view.shape[1])
    ax.set_ylim(0, map_thermal_view.shape[0])
    ax.set_aspect('equal')
    ax.grid(False)
    ax.set_title(f"{title} - Hour: {hour}")
    plt.colorbar(img, ax=ax, label="Thermal Value (0 to 30)")  # Add colorbar to show thermal scale
