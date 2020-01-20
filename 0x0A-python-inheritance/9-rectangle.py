#!/usr/bin/python3
"""Module which contians a rectange class based off of the BaseGeometry
class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Basic rectangle function"""

    def __init__(self, width, height):
        """Init function with width and height"""

        try:
            self.integer_validator("width", width)
        except Exception as e: raise
        else:
            self.__width = width

        try:
            self.integer_validator("height", height)
        except Exception as e: raise
        else:
            self.__height = height

    def area(self):
        """Function which returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Gets the string version of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """Prints out info on the rectangle"""

        print(self)
