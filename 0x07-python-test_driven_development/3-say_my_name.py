#!/usr/bin/python3
"""
This module contains a test-proven name-saying function

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""


def say_my_name(first_name, last_name=""):
    """Prints out ``My name is <first name> <last name>``

    Args:
        first_name (str): The first name to be printed
        last_name (str): The last name to be printed
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
