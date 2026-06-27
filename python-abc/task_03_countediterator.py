#!/usr/bin/env python3
"""Module that defines a counted iterator."""


class CountedIterator:
    """Iterator that counts the number of iterated items."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of iterated items."""
        return self.count
