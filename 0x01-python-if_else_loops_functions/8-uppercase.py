#!/usr/bin/python3
def uppercase(strn):
    for i in range(len(strn)):
        c = ord(strn[i])
        if (c >= 97) and (c <= 122):
            c -= 32
        c = chr(c)
        print("{}".format(c), end="")
    print()
