from items import Item, House, Tree, Road, Pond, Lake, Animal  # Import the required item classes

class Block:
    def __init__(self, position):
        self.position = position
        self.items = [Item(position, "Grass", (34, 139, 34))]  # Default item is Grass with a green color

    def add_item(self, item):
        """Add a new item to the block."""
        self.items.append(item)

    def get_rgb(self):
        """Get the RGB color of the last item added to the block."""
        return self.items[-1].get_rgb()

    def get_thermal(self, temp):
        """Calculate the average thermal properties of all items in the block based on the given temperature."""
        return sum(item.get_thermal(temp) for item in self.items) / len(self.items)

    def modify_item(self, item_name, **kwargs):
        """
        Modify the attributes of a specific item in the block.
        
        You can update position, color, thermal conductivity, or size (for houses).
        """
        for item in self.items:
            if item.name == item_name:
                if "position" in kwargs:
                    item.set_position(kwargs["position"])  # Update position if provided
                if "color" in kwargs:
                    item.set_color(kwargs["color"])  # Update color if provided
                if "thermal_conductivity" in kwargs:
                    item.set_thermal_conductivity(kwargs["thermal_conductivity"])  # Update thermal conductivity
                if isinstance(item, House) and "size" in kwargs:
                    item.set_size(*kwargs["size"])  # Update house size if provided
                return  # Exit the loop after modifying the item
