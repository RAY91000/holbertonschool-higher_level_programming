#!/usr/bin/python3
"""
Define function to check if a object is a instance of a class or its subclass.

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or its subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
