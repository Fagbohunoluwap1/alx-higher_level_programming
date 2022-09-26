#!/usr/bin/python3
"""Finds if an object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Function to determine if exactly an object is an instance of a class

    Args:
        obj: object to look at
        a_class: class to verify if an object is an instance of.

    Return:
        True if object is an instance of a class
        otherwise False.
    """

    return True if type(obj) is a_class else false
