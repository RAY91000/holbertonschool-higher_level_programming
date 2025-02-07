#!/usr/bin/python3
"""
VerboseList class
"""


class VerboseList(list):
    """
    Custom list class that provides notifications when items are added
    or removed.
    """
    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with multiple items and prints a notification."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns an item from the list and prints a
        notification."""
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
