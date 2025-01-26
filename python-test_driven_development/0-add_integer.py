#!/usr/bin/python3
'''This modules provides a function to perform
    integer addition.
    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
'''


def add_integer(a, b=98):
    """
    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
