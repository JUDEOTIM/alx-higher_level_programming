#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a
    string and its first character."""
    count = len(sentence)
    if count == 0:
        return (0, None)
    return (count, sentence[0])
