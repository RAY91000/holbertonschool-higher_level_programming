#!/usr/bin/python3

"""
BaseGeometry class
"""


class BaseGeometry:
    """
    A class representing base geometry with validation methods.

    Public instance methods:
        - area: raises an exception if not implemented in a subclass.
        - integer_validator: validates integer values.
    """

    def area(self):
        """
        Raises an exception because the area method is not implemented.

        Raises:
            Exception: with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's a positive integer.

        Args:
            name (str): the name to be used in error messages.
            value (int): the value to be validated.

        Raises:
            TypeError: if value is not an integer or is a boolean.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if name is None or not isinstance(name, str):
            raise TypeError("name must be a string")
        if value is None:
            raise TypeError(f"{name} must be an integer")


"""
Rectangle class that inherits from BaseGeometry.

This class defines a rectangle by its width and height, both of which are
positive integers validated by the integer_validator method. Iy
implements
the area() method to calculate the area of the rectangle and overrides
the __str__ method to provide the rectangle's description in the format
"[Rectangle] width/height".
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    This class defines a rectangle with width and height attributes, both of
    which are validated to be positive integers. It includes a method to
    calculate the area of the rectangle and overrides the __str__ method to
    provide the rectangle's description in format "[Rectangle]width/height".
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)  # Validate width
        super().integer_validator("height", height)  # Validate height
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
