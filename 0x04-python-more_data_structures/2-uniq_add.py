#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list
       (only once for each integer)."""

    total = 0
    for n in set(my_list):
        total += n

    return total
