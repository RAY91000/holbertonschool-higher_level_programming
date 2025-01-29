#!/usr/bin/python3
"""A class representing a square with size validation."""

class Square:
    """
    A class that defines a square with a private instance attribute: size.

    Attributes:
        __size (int): The size of the square (must be an integer and >= 0).
    """

    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
