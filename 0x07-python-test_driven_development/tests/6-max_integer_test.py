#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-3, 4, 2, -9]), 4)
        self.assertEqual(max_integer([4], 4))

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_weird_types(self):
        self.assertEqual(max_integer("foo"), "o")
        self.assertEqual(max_integer([1.5, 3.9, 2.2]), 3.9)

    def test_fails(self):
        with self.assertRaises(TypeError):
            max_integer(47)

        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, 3.5, -2]), 3.5)

        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])
