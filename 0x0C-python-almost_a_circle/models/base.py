#!/usr/bin/python3
"""This module contains a base class for all shape objects"""


class Base():
    """This is a base class for all shape objects which keeps track of IDs"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
