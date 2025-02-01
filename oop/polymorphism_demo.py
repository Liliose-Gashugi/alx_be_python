import math

class Shape:
    def area(self):
        """
        Calculate the area of the shape.
        This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize a Rectangle with a given length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Formula: π * radius^2
        """
        return math.pi * (self.radius ** 2)