#!/usr/bin/python3
"""This module contains a function that checks if the type of an object is a
subclass (directly or indirectly) of an other class"""


def inherits_from(obj, a_class):
    """Checks if `a_class` is a parent of `obj` type"""

    return isinstance(obj, a_class) and type(obj) is not a_class
