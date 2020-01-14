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

    @width.setter
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
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function to get the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Function to get the perimeter of the rectangle"""
        if self.width is 0 or self.height is 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        ret = ""
        for x in range(self.height):
            ret += "#" * self.width + ("\n" if x != self.height - 1 else "")
        return ret

    def print(self):
        print(str(self))
