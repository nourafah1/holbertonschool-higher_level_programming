#!/usr/bin/python3
"""Module that defines MyList."""


class MyList(list):
    """Class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
