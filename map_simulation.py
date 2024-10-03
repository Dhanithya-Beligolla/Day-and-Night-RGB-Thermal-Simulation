import numpy as np
from blocks import Block

class MapSimulation:
    def __init__(self, width, height):
        # Initialize a 2D grid of blocks for the map
        self.width = width
        self.height = height
        self.blocks = [[Block((i, j)) for j in range(width)] for i in range(height)]  # Create blocks based on grid size

    def add_items_to_block(self, x, y, items):
        """
        Add a list of items to the block at the given (x, y) position.
        
        Raises an IndexError if the coordinates are out of bounds.
        """
        if 0 <= x < len(self.blocks) and 0 <= y < len(self.blocks[0]):  # Ensure (x, y) is within map bounds
            self.blocks[x][y].items.extend(items)  # Add items to the block
        else:
            raise IndexError(f"Coordinates ({x}, {y}) are out of bounds.")  # Handle out-of-bounds error

    def generate_rgb_view(self):
        """Generate a 2D array of RGB values representing the entire map view."""
        return np.array([[block.get_rgb() for block in row] for row in self.blocks])  # Return RGB data for all blocks

    def generate_thermal_view(self, temp):
        """Generate a 2D array of thermal values for the entire map based on the given temperature."""
        return np.array([[block.get_thermal(temp) for block in row] for row in self.blocks])  # Return thermal data for all blocks

    def modify_item_in_block(self, x, y, item_name, **kwargs):
        """
        Modify the attributes of an item in a specific block at position (x, y).
        
        Ensures the block exists within the map before attempting to modify the item.
        """
        if 0 <= x < self.height and 0 <= y < self.width:  # Check if (x, y) is within map boundaries
            self.blocks[x][y].modify_item(item_name, **kwargs)  # Modify the item in the specified block
