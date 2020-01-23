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
        """Tests proper initialization

        TODO: improper number of args
        """
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

    def test_illegal_dimension_types(self):
        """Tests for correct handling of illegal dimension attributes"""
        with self.assertRaises(TypeError) as err:
            Rectangle("foo", 1)
            self.assertEqual(err.msg, "width must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(None, 1)
            self.assertEqual(err.msg, "width must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(float("inf"), 1)
            self.assertEqual(err.msg, "width must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, "foo")
            self.assertEqual(err.msg, "height must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, None)
            self.assertEqual(err.msg, "height must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, float("inf"))
            self.assertEqual(err.msg, "height must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(None, float("inf"))
            self.assertEqual(err.msg, "width must be an integer")

    def test_illigal_dimension_values(self):
        """Tests for correct handling of illegal dimension values"""
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 5)
            self.assertEqual(err.msg, "width must be > 0")

        with self.assertRaises(ValueError) as err:
            Rectangle(-9, 5)
            self.assertEqual(err.msg, "width must be > 0")

        with self.assertRaises(ValueError) as err:
            Rectangle(5, 0)
            self.assertEqual(err.msg, "height must be > 0")

        with self.assertRaises(ValueError) as err:
            Rectangle(5, -9)
            self.assertEqual(err.msg, "height must be > 0")

        with self.assertRaises(ValueError) as err:
            Rectangle(-9, -10)
            self.assertEqual(err.msg, "width must be > 0")

    def test_illegal_coordinate_types(self):
        """Tests for correct handling of illegal coordinate types"""
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, x="foo")
            self.assertEqual(err, "x must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, x=None)
            self.assertEqual(err, "x must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, x=float("inf"))
            self.assertEqual(err, "x must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, y="foo")
            self.assertEqual(err, "y must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, y=None)
            self.assertEqual(err, "y must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, y=float("inf"))
            self.assertEqual(err, "y must be an integer")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, x=None, y=float("inf"))
            self.assertEqual(err, "x must be an integer")

    def test_illegal_coordinate_values(self):
        """Tests for correct handling of illegal coordinate values"""
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, x=-1)
            self.assertEqual(err, "x must be >=0")

        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, y=-1)
            self.assertEqual(err, "y must be >=0")

        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, x=-5, y=-1)
            self.assertEqual(err, "x must be >=0")

    def test_area(self):
        """Tests the area instance method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
