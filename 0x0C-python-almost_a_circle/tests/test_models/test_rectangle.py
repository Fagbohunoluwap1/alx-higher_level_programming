#!/usr/bin/python3
"""Defines unittest for models/rectangle.py.

Unittest classes:
    TestRectangle - line 15
    """

import unittest
import io
import sys
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases forn the rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """Test Rectangle class: check for id."""

        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r4.id, -5)

    def test_2_1(self):
        """Test Rectangle class: check for attributes values."""

        r1 = Rectangle(12, 5)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(12, 5, 7, 9, 34)
        self.assertEqual(r2.width, 12)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 9)

    def test_2_2(self):
        """Test Rectangle class: check for missing arguments."""

        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(s, str(x.exception))

        def test_2_3(self):
            """Test class Rectangle: check for inheritance."""

        r1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_3_0(self):
        """Test class Rectangle: check for attributes."""

        with self.assertRaises(TypeError):
            Rectangle()
