#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This class is a rectangle based off of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): The X position of the rectangle
            y (int, optional): The Y position of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """Getter for the private `x` attribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """Setter for the private `x` attribute"""
        self.__x = val

    @property
    def y(self):
        """Getter for the private `y` attribute"""
        return self.__y

    @y.setter
    def y(self, val):
        """Setter for the private `y` attribute"""
        self.__y = val

    @property
    def width(self):
        """Getter for the private `width` attribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter for the private `width` attribute"""
        self.__width = val

    @property
    def height(self):
        """Getter for the private `height` attribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """Setter for the private `height` attribute"""
        self.__height = val
