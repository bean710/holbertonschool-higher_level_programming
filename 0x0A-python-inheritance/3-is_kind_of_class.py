#!/usr/bin/python3
"""This module contains a function to determine if an object is an instance of
a class or any class which inherits it"""


def is_kind_of_class(obj, a_class):
    """Function that returns whether an object is an instance of a class"""

    return isinstance(obj, a_class)
