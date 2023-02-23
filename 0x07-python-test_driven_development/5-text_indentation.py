#!/usr/bin/python3
"""Defines a function to indent text."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?',       and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        if text[ch] in "\n.?:":
            if text[ch] in ".?:":
                print(text[ch])
            print("")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        print(text[ch], end="")
        ch += 1
