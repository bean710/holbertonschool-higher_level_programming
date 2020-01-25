"""This module tests the Square class using unittests"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    def setUp(self):
        """Resets the class to prevent interference"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Tests that squares are initialized properly"""
        s1 = Square(4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 2, 3, 47)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.id, 47)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_str(self):
        """Tests that str() prints a nice version of the square"""
        s1 = Square(4, 2, 3, 47)
        self.assertEqual(str(s1), "[Square] (47) 2/3 - 4")

    def test_size(self):
        """Tests that the size of a square can be gotten and set"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 9
        self.assertEqual(s1.size, 9)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "foo"
