#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        result = fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        result = None
    return result
