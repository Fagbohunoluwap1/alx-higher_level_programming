#!/usr/bin/python3
"""Defines a append writting function"""


def append_write(filename="", text=""):
    """Appends a string at the end of text file UTF8.

    Args:
        filename (str): The name of the file to append
        text (str): The text to append.

    Returns:
        The numbers of character added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
