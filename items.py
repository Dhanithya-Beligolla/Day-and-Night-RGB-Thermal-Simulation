class Item:
    def __init__(self, position, name, color, thermal_conductivity=1.0):
        """
        Base class for all items in the map simulation.

        Args:
            position (tuple): (x, y) coordinates of the item.
            name (str): Name of the item.
            color (tuple): RGB color of the item.
            thermal_conductivity (float): The thermal conductivity value (default is 1.0).
        """
        self.position = position
        self.name = name
        self.color = color
        self.thermal_conductivity = thermal_conductivity

    def get_rgb(self):
        """Returns the RGB color of the item."""
        return self.color

    def get_thermal(self, temp):
        """Calculates the thermal property of the item based on the given temperature."""
        return temp * self.thermal_conductivity

    def set_position(self, new_position):
        """Sets a new position for the item."""
        self.position = new_position

    def set_color(self, new_color):
        """Sets a new RGB color for the item."""
        self.color = new_color

    def set_thermal_conductivity(self, new_conductivity):
        """Sets a new thermal conductivity for the item."""
        self.thermal_conductivity = new_conductivity


class Tree(Item):
    def __init__(self, position, radius=0.25):
        """
        A class representing a tree in the simulation.

        Args:
            position (tuple): (x, y) coordinates of the tree.
            radius (float): The radius of the tree (default is 0.25).
        """
        super().__init__(position, "Tree", (0, 100, 0))  # Dark green color for trees
        self.radius = radius  # Radius for the tree

    def set_radius(self, new_radius):
        """Sets a new radius for the tree."""
        self.radius = new_radius


class House(Item):
    def __init__(self, position, width=3, length=2):
        """
        A class representing a house in the simulation.

        Args:
            position (tuple): (x, y) coordinates of the house.
            width (int): Width of the house (default is 3).
            length (int): Length of the house (default is 2).
        """
        super().__init__(position, "House", (139, 69, 19))  # Brown color for houses
        self.width = width  # Width of the house
        self.length = length  # Length of the house

    def set_size(self, new_width, new_length):
        """Sets new dimensions for the house."""
        self.width = new_width
        self.length = new_length


class Road(Item):
    def __init__(self, position, width=1):
        """
        A class representing a road in the simulation.

        Args:
            position (tuple): (x, y) coordinates of the road.
            width (int): Width of the road (default is 1).
        """
        super().__init__(position, "Road", (128, 128, 128))  # Gray color for roads
        self.width = width  # Width of the road

    def set_width(self, new_width):
        """Sets a new width for the road."""
        self.width = new_width


class Pond(Item):
    def __init__(self, position, radius=1):
        """
        A class representing a pond in the simulation.

        Args:
            position (tuple): (x, y) coordinates of the pond.
            radius (float): The radius of the pond (default is 1).
        """
        super().__init__(position, "Pond", (0, 0, 255))  # Blue color for ponds
        self.radius = radius  # Radius for the pond

    def set_radius(self, new_radius):
        """Sets a new radius for the pond."""
        self.radius = new_radius


class Lake(Item):
    def __init__(self, position):
        """
        A class representing a lake in the simulation.

        Args:
            position (tuple): (x, y) coordinates of the lake.
        """
        super().__init__(position, "Lake", (0, 0, 255))  # Blue color for lakes




class Animal(Item):
    def __init__(self, position):
        """
        A class representing an animal in the simulation.

        Args:
            position (tuple): (x, y) coordinates of the animal.
        """
        super().__init__(position, "Animal", (255, 0, 0))  # Red color for animals


