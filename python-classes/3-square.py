#!/usr/bin/python3
"""
A class to represent a square.

Attributes:
-----------
__size : int
    The size of the square's side (private attribute).

Methods:
--------
__init__(size=0):
    Initializes a square with a given size.

area():
    Returns the area of the square.
"""


class Square:
    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Parameters:
        -----------
        size : int, optional
            The size of the square's side (default is 0).

        Raises:
        -------
        TypeError
            If size is not an integer.
        ValueError
            If size is negative.
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
        return self.__size * self.__size
