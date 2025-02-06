#!/usr/bin/python3
"""Defines a subclass of list with a method to print a sorted version.
"""


class MyList(list):
    """A subclass of list that includes a method to print a sorted list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
