#!/usr/bin/python3
""" Print_square module
"""


def print_square(size):
    """Print Square
    Args:
        size (int or float): Description
    Raises:
        TypeError: Size must be an integer
        ValueError: Size must be >= 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(int(size)):
        print("#" * int(size))
