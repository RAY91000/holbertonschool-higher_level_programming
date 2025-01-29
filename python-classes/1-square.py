#!/usr/bin/python3
class Square:
    """
    A class that defines a square with a private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size: The size of the square.
        """
        self.__size = size  # Private instance attribute
