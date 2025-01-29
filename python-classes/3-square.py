#!/usr/bin/python3
"""
A class to represent a square.

"""

class Square:
    """
    A class that defines a square with a private instance attribute: size.
    It includes a method to compute the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
         """
        Calculates and returns the area of the square.

        Returns:
        --------
        int
            The area of the square.
        """
        return self.__size ** 2
