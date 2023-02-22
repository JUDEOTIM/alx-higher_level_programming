#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if isinstance(a_dictionary, dict) and len(a_dictionary) != 0:
        key = list(a_dictionary.keys())[0]
        best_score = a_dictionary[key]
        for k, v in a_dictionary.items():
            if v > best_score:
                best_score = v
                key = k
        return (key)
