#!/usr/bin/python3
"""Defines a class Square that inherits from 9-rectangle.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a rectangle using square."""

    def __init__(self, size):
        """Initialize  a new Rectangle.

        Args:
            size (int): size of the new integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
