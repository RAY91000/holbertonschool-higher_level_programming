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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
