#!/usr/bin/python3
"""Finds if an object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an inherited instance of a class.

    Args:
        obj: object to check
        a_class: The class to map the type of object to.

    Returns:
        If obj is an inherited instance of a class - True.
        Otherwise - False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
