#!/usr/bin/python3
"""Module that checks if an object is an instance of a class that inherited
from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance to.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
