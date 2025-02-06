#!/usr/bin/python3
"""
Module that defines the Square class inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Size must be a positive integer, validated by integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the Square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Computes the area of the Square.
        """
        return self.__size * self.__size
