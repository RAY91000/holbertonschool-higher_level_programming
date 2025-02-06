#!/usr/bin/python3
"""
Defines a function to check if an object is an instance of a specific class.

"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
