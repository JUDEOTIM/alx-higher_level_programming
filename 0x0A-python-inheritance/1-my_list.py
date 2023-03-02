#!/usr/bin/python3
"""Defines a class MyList that inherits from the list class."""

class MyList(list):
    """Implements sorted printing."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
