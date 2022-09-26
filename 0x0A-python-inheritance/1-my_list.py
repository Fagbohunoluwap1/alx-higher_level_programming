#!/usr/bin/python3
"""Creates a class that inherits from list class."""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Print a list in ascending sort."""
        print(sorted(self))
