#!/usr/bin/python3
"""A class representing a square with size validation."""


class Square:
    """A class representing a square with size validation."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private attribute
