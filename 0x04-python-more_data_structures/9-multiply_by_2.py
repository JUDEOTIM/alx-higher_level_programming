#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2
    """
    dict_by_2 = a_dictionary.copy()
    for key in dict_by_2.keys():
        dict_by_2[key] *= 2

    return dict_by_2
