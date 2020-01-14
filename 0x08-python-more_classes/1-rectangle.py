#!/usr/bin/python3
"""
This module has a simple rectangle class
"""


class Rectangle:
    """Basic rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional height and width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for rectangle width"""
        return self.__width

    @set.width
    def width(self, value):
        """Setter for rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for rectangle height"""
        return self.__width

    @set.height
    def height(self, value):
        """Setter for rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
