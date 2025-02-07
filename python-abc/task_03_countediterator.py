#!/usr/bin/python3
"""
countediterator class
"""


class CountedIterator:
    """
    Custom iterator that keeps track of the number of items iterated over.
    """
    def __init__(self, iterable):
        """Initializes the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Returns the iterator object."""
        return self

    def __next__(self):
        """Returns the next item and increments the counter."""
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Returns the number of items iterated over."""
        return self.count
