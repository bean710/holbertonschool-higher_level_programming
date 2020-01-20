"""This module contains a function which tells if an object is of exactly the
same class as the second argument"""


def is_same_class(obj, a_class):
    """Checks if `obj` is of exactly the class `a_class`"""

    return type(obj).__name__ == a_class
