#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))

    for i in range(length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
