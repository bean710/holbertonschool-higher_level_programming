#!/usr/bin/python3
"""Module for testing the Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests the Base class"""

    def setUp(self):
        """Resets the base class to prevent interference"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Tests proper initialization"""
        a = Base()
        self.assertEqual(type(a), Base)
        b = Base(47)
        self.assertEqual(type(b), Base)

    def test_id(self):
        """Tests that the correct IDs are being assigned"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(47)
        self.assertEqual(b.id, 47)
        c = Base()
        self.assertEqual(c.id, 2)
