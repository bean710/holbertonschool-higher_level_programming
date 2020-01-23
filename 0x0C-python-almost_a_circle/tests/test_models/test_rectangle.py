#!/usr/bin/python3
"""Module for testing the Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Tests the Rectangle class"""

    def setUp(self):
        """Resets the class to prevent interference"""
        Base._Base__nb_objects = 0

    def test_class_setup(self):
        """Tests to make sure Rectangle inherits Base"""
        self.assertTrue(issubclass(Rectangle, Base))
        a = Rectangle(1, 1)
        self.assertTrue(isinstance(a, Base))

    def test_init(self):
        """Tests proper initialization"""
        a = Rectangle(1, 1)
        self.assertEqual(type(a), Rectangle)
        b = Rectangle(1, 1, 3)
        self.assertEqual(type(b), Rectangle)
        c = Rectangle(1, 1, 3, 4)
        self.assertEqual(type(c), Rectangle)
        d = Rectangle(1, 1, 3, 4, 29)
        self.assertEqual(type(d), Rectangle)
        e = Rectangle(width=1, height=1, x=3, y=4, id=29)
        self.assertEqual(type(e), Rectangle)

    def test_id(self):
        """Tests that the correct IDs are being assigned"""
        a = Rectangle(1, 1)
        self.assertEqual(a.id, 1)
        b = Rectangle(1, 1, id=47)
        self.assertEqual(b.id, 47)
        c = Rectangle(1, 1)
        self.assertEqual(c.id, 2)

    def test_dimensions(self):
        """Tests that the rectangle's dimensions are handled properly

        This test makes sure that the dimensions are assigned correctly during
        init, but also when changed manually. Also makes sure the other
        dimension is not changed when the other is modified

        """
        a = Rectangle(1, 2)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        a.width = 4
        self.assertEqual(a.width, 4)
        self.assertEqual(a.height, 2)
        a.height = 5
        self.assertEqual(a.height, 5)
        self.assertEqual(a.width, 4)

    def test_coordinates(self):
        """Tests that the rectangle's coordinates are handled properly

        This test makes sure that the coordinates are assigned correctly
        during init, but also when changed manually. Also makes sure the other
        coordinate is not changed when the other is modified

        """
        a = Rectangle(1, 1)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        b = Rectangle(1, 1, 2, 3)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 3)
        b.x = 4
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 3)
        b.y = 5
        self.assertEqual(b.y, 5)
        self.assertEqual(b.x, 4)
