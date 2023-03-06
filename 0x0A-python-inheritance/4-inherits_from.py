#!/usr/bin/python3
""" Inherits from module
"""


def inherits_from(obj: object, a_class: object) -> bool:
    """ inherits from module, checks if an object inherit from
    a base class
    Args:
        obj (object): object arg to compare
        a_class (object): object arg to compare
    Returns:
        bool: Description
    """
    obj_type = type(obj)
    if (obj_type != a_class):
        return issubclass(type(obj), a_class)
    else:
        return False
