#!/usr/bin/python3
def islower(c):
    """write a function that checks for lower case characters."""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
