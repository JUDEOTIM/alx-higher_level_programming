#!/usr/bin/python3

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""

    if isinstance(my_list, list) and len(my_list) != 0:
        score = 0
        weight_total = 0
        for a_tuple in my_list:
            score += (a_tuple[0] * a_tuple[1])
            weight_total += a_tuple[1]
        return (score / weight_total)
    return (0)
