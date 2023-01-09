#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all characters c and C from a
    string.
    """
    copy = [c for c in my_string if c not in ["C", "c"]]
    return ("".join(copy))
