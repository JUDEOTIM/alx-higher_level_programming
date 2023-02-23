#!/usr/bin/python3
""" Say My Name module
"""


def say_my_name(first_name, last_name="") -> None:
    """Summary
    Args:
        first_name (str): first name
        last_name (str, okptional): Last name
    Raises:
        TypeError: Name Must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
