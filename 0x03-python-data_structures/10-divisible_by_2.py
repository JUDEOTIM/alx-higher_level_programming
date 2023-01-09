#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    copy = [True if (n % 2) == 0 else False for n in my_list]
    return copy
