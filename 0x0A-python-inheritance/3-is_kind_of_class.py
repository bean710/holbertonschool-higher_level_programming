"""This module contains a function to determine if an object is an instance of
a class or any class which inherits it"""


def is_kind_of_class(obj, a_class):
    """Function that returns whether an object is an instance of a class"""

    return any(x.__name__ == a_class for x in type(obj).__bases__)\
            or type(obj).__name__ == a_class
