#!/usr/bin/python3
"""  Add attr module
"""


def add_attribute(obj, a, v):
    """ Adds attr to an object
    Args:
        obj (object): object
        a (str): attr arg
        v (str): attr arg
    Raises:
        TypeError: can't add new attribute
    """
    res = getattr(obj, "__dict__", None)
    if res == {}:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
