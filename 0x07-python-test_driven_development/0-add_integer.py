#!/usr/bin/python3
"""
This module contains a test-proven addition function

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""


def add_integer(a, b=98):
    """Adds two numbers (int or float) together

    In the case of a float passed to the function, it will be cast to an int
    and therefore floor'd

    Args:
        a (int): The first number
        b (int, optional): The second number

    Returns:
        int: The sum of both values

    """

    if not isinstance(a, (int, float)) or a != a or a == float("inf"):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or b == float("inf"):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
