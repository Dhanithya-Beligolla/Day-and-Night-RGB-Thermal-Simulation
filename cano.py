import numpy as np
from map_simulation import MapSimulation
from items import Tree, House, Road, Pond, Lake, Animal
from visuals import plot_map_rgb, plot_map_thermal
import matplotlib.pyplot as plt

# Helper function to check for collisions
def check_collision(x, y, occupied_positions):
    """Ensure items do not overlap."""
    return (x, y) in occupied_positions

# Define temperature for each hour of the day (example curve)
def get_hourly_temperature(hour):
    """Return a temperature for the given hour of the day."""
    # Warmer during the day, cooler at night, with a peak around 12 PM (midday)
    if 6 <= hour <= 18:  # Warmer temperatures during the day
        return 10 + (15 * np.sin(np.pi * (hour - 6) / 12))  # Peak at noon
    else:  # Cooler temperatures at night
        return 5 + (5 * np.sin(np.pi * (hour - 18) / 12))  # Drop in the evening/night

# Simulate a full day with hourly RGB and thermal views
def simulate_full_day(simulation_map):
    """Simulate and plot RGB and thermal views for each hour of the day."""
    
    for hour in range(24):  # Loop through each hour of the day
        temp = get_hourly_temperature(hour)  # Get the temperature for the hour
        rgb_view = simulation_map.generate_rgb_view()
        thermal_view = simulation_map.generate_thermal_view(temp)
        
        # Create a new figure with 2 subplots: one for RGB and one for Thermal
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle(f"Hour {hour}: RGB and Thermal Views")

        # Plot RGB view with dynamic brightness
        axes[0].set_title(f"RGB View - Hour {hour}")
        plot_map_rgb(rgb_view, simulation_map.blocks, hour, ax=axes[0])

        # Plot Thermal view with dynamic temperature and color contrast
        axes[1].set_title(f"Thermal View - Hour {hour}, Temp: {temp:.1f}°C")
        plot_map_thermal(thermal_view, simulation_map.blocks, temp, ax=axes[1])
        
        # Display the figure for this hour
        plt.show()



def main():
    width, height = 50, 36   # Increased map size to avoid out-of-bound errors
    simulation_map = MapSimulation(width, height)
    occupied_positions = set()  # Set to track occupied positions

    # Add houses (brown rectangle)
    house_positions = [(6, 3),(6,20)]  # Two houses on the left side
    for x, y in house_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [House((x, y), width=8, length=4)])  # Larger houses
            occupied_positions.add((x, y))
    
    ##### for Palace
    # Add palace long (brown rectangle)
    house_positions = [(20, 2), (31, 2)]  # Two houses on the left side
    for x, y in house_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [House((x, y), width=12, length=4)])  # Larger houses
            occupied_positions.add((x, y))

    # Add palace midle (brown rectangle)
    house_positions = [(27, 2),(9,2)]  # Two houses on the left side
    for x, y in house_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [House((x, y), width=5, length=7)])  # Larger houses
            occupied_positions.add((x, y))

    # Add roads (gray paths in the screenshot)
    road_positions = [(i, 33) for i in range(35)] + [(13, j) for j in range(33)] + [(34, l) for l in range(33)]  # Two crossing roads
    for x, y in road_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [Road((x, y), width=2)])  # Roads at specific positions
            occupied_positions.add((x, y))

    # Add trees (dark green circles)
    tree_positions = [
        # Trees on the left side
        (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),
        (15,1),(15,2),(15,3),(15,4),(15,5),(15,6),(15,7),(15,8),(15,9),(15,10),(15,11),(15,12),(15,13),(15,14),(15,15),(15,16),(15,17),(15,18),(15,19),(15,20),(15,21),(15,22),(15,23),(15,24),(15,25),(15,26),(15,27),(15,28),(15,29),(15,30),(15,31),
        (33,1),(33,2),(33,3),(33,4),(33,5),(33,6),(33,7),(33,8),(33,9),(33,10),(33,11),(33,12),(33,13),(33,14),(33,15),(33,16),(33,17),(33,18),(33,19),(33,20),(33,21),(33,22),(33,23),(33,24),(33,25),(33,26),(33,27),(33,28),(33,29),(33,30),(33,31),



        # Left Houses tree
        (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),
        (12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,11),(12,12),(12,13),
        (1,14),(2,14),(3,14),(4,14),
        (1,15),(2,15),(3,15),(4,15),
        (1,16),(2,16),(3,16),(4,16),
        (10,14),(11,14),(12,14),
        (10,15),(11,15),(12,15),
        (10,16),(11,16),(12,16),
        
        # Right Houses tree
        (1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),(1,24),(1,25),(1,26),(1,27),(1,28),(1,29),(1,30),
        (1,31),(2,31),(3,31),(4,31),(5,31),(6,31),(7,31),(8,31),(9,31),(10,31),(11,31),(12,31),
        (12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,26),(12,27),(12,28),(12,29),(12,30),

        # Palace trees
        (18,15),(18,16),(18,17),(18,18),(18,19),(18,20),(18,21),(18,22),(18,23),(18,24),(18,25),(18,26),(18,27),(18,28),(18,29),(18,30),
        (19,15),(19,16),(19,17),(19,18),(19,19),(19,20),(19,21),(19,22),(19,23),(19,24),(19,25),(19,26),(19,27),(19,28),(19,29),(19,30),

        (22,13),(26,13),(22,8),(26,8),

        (29,15),(29,16),(29,17),(29,18),(29,19),(29,20),(29,21),(29,22),(29,23),(29,24),(29,25),(29,26),(29,27),(29,28),(29,29),(29,30),
        (30,15),(30,16),(30,17),(30,18),(30,19),(30,20),(30,21),(30,22),(30,23),(30,24),(30,25),(30,26),(30,27),(30,28),(30,29),(30,30),

        (16,31),(17,31),(18,31),(19,31),(20,31),(21,31),(22,31),
        (26,31),(27,31),(28,31),(29,31),(30,31),(31,31),(32,31),

   

        # Trees Forest
        (27, 43), (29, 40), (30, 46), (26, 47), (28, 46), (26, 42), (34, 48), (28, 42), (32, 49), (32, 46), (33, 45), (31, 44), (27, 48), (27, 44), (31, 45), (32, 41), (30, 43), (31, 48), (29, 44), (31, 46),(30, 47), (26, 44), (29, 48), (28, 48), (29, 48), (34, 44), (30, 40), (30, 40), (33, 45), (31, 44), (29, 43), (31, 45), (27, 44), (27, 41), (28, 42), (26, 48), (34, 46), (26, 43), (32, 40), (30, 49),(30, 43), (32, 47), (30, 42), (32, 44), (28, 43), (26, 48), (33, 46), (31, 49), (29, 48), (27, 41), (32, 47), (32, 44), (26, 42), (27, 44), (33, 46), (32, 45), (28, 41), (33, 49), (32, 48), (33, 46), (27, 40), (26, 44), (32, 45), (29, 48), (29, 48), (27, 49), (27, 48), (31, 42), (26, 43), (34, 46), (27, 40), (31, 45), (30, 46), (33, 48), (26, 47), (31, 40), (27, 45), (34, 45), (34, 40), (26, 48), (30, 47), (32, 48), (26, 44), (32, 47), (29, 43), (31, 47),

        # Random trees
        (16, 49), (6, 47), (20, 44), (15, 40), (22, 42), (17, 47), (5, 40), (22, 49), (20, 43), (12, 47),(13, 42), (3, 41), (1, 43), (6, 43), (21, 42), (12, 45), (11, 47), (11, 44), (19, 49), (17, 46),(4, 45), (20, 41), (18, 45), (17, 42), (22, 47), (21, 41), (3, 40), (21, 40), (12, 48), (18, 48),(7, 40), (1, 44), (4, 43), (8, 44), (4, 46), (3, 44), (12, 46), (14, 41), (7, 49), (14, 43),(23, 48), (4, 44), (2, 48), (4, 48), (21, 47), (11, 40), (24, 45), (12, 40), (11, 41), (24, 43),(8, 42), (17, 48), (16, 46), (21, 44)


        
    ]
    for x, y in tree_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [Tree((x, y), radius=0.38)])  # Cluster of trees
            occupied_positions.add((x, y))

    # Add ponds (blue circles)
    pond_positions = [(7, 15), (24, 10)]  # Ponds in specific places
    for x, y in pond_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [Pond((x, y), radius=2)])  # Medium-sized ponds
            occupied_positions.add((x, y))

    # Add animals (red circles)
    animal_positions = [(10, 46), (17, 49), (16, 44), (3, 45), (6, 42), (11, 45), (23, 42), (22, 49), (17, 47), (1, 45), (5, 40), (24, 42), (12, 49), (22, 47), (10, 49), (9, 42), (8, 40), (14, 48), (11, 44), (15, 49),  (20, 44), (12, 48), (22, 49), (5, 44), (8, 45), (17, 49), (24, 41), (16, 49), (16, 46), (16, 46),  (8, 41), (24, 46), (20, 43), (6, 43)]

    for x, y in animal_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [Animal((x, y))])
            occupied_positions.add((x, y))

    # Add a river (blue rectangle)
    river_start_x, river_start_y = 0, 35  # Start coordinates for the river
    river_width, river_length = 36, 3  # River along the middle of the map

    for x in range(river_start_x, river_start_x + river_width):
        for y in range(river_start_y, river_start_y + river_length):
            if not check_collision(x, y, occupied_positions):
                simulation_map.add_items_to_block(x, y, [Pond((x, y), radius=0)])  
                occupied_positions.add((x, y))

    # Add Smll Roads (small gey rectangles)
    bridge_positions = [(24,15),(23,15),(23,18),(24,18),(23,21),(24,21),(23,24),(24,24),(23,27),(24,27),(23,30),(24,30),(12,9),(11,9),(10,9),(9,9),(8,9),(8,24),(9,24),(10,24),(11,24),(12,24)]  # Small roads
    for x, y in bridge_positions:
        if not check_collision(x, y, occupied_positions):
            simulation_map.add_items_to_block(x, y, [Road((x, y), width=2)])  
            occupied_positions.add((x, y))

    # Simulate the full day (24 hours)
    simulate_full_day(simulation_map)


if __name__ == "__main__":
    main()

