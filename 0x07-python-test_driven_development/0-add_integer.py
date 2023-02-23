#!/usr/bin/python3
""" Add integer modules
    Adds two number floats or int
    """


def add_integer(a, b=98):
    """Adds two number floats or int
    Args:
        a (int, float): first argument
        b (int, float, optional): _description_. Defaults to 98.
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Returns:
        int: the sum of integer a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
