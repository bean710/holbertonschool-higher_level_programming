#!/usr/bin/python3
"""This module is a test-proven square-printer

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""


def print_square(size):
    """Prints a square of #s size ``size``

    Args:
        size (int): The size (side length) of the square to be printed
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
        return

    for height in range(size):
        print("#" * size)
