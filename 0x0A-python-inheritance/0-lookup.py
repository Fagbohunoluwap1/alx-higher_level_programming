#!/usr/bin/python3
"""Finding a list of available objects and methods of an object"""


def lookup(obj):
    """Returns the list of attributes and methods.

    Args:
        obj: object to look into
    """

    return dir(obj)
