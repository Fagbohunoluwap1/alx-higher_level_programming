#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:
    TestBase - line 17
"""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """Create new instances: check for id."""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(789)
        self.assertEqual(b4.id, 789)
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def test_1_1(self):
        """Test for type and instance."""

        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))
