#!/usr/bin/python3
"""
Module that defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
        (excluding the class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
