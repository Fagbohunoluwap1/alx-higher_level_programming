#!/usr/bin/python3
"""Finds if an object is an instance of,or if the object is an instance of a class inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """Function to determine if an object is an instance of a_class or a class inherited from a_class

    Args:
        obj: object to look at.
        a_class: class to evaluate

    Return:
        If obj is an instance  or inherited instance of a_class - True
        otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
