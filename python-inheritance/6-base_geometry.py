#!/usr/bin/python3
"""
BaseGeometry class with an unimplemented area method.

"""


class BaseGeometry:
    """Class representing geometric shapes."""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
