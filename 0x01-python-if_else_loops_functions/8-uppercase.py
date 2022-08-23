#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= ('a') and ord(c) <= ('z'):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{:s}".format(char), end="")
    print('')
