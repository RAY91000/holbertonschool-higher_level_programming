#!/usr/bin/python3

""" aaaaaaaaa """


class Rectangle:
    """
    A class that defines a rectangle with width and height.

    Attributes:
        number_of_instances (int): Counter for Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of the rectangle or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.__width for _ in range(self.__height)
        )

    def __repr__(self):
        """Returns string representation to recreat new instance use eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message and decrements instance counter when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on the area.
        If both have the same area, returns rect_1.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
