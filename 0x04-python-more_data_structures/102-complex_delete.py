#!/usr/bin/python3
"""Defines a function that deletes recurring values from
   dictionary."""


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for key in a_dictionary.keys():
            if a_dictionary[key] == value:
                del a_dictionary[key]
                break

    return (a_dictionary)
