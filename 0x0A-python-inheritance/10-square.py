#!/usr/bin/python3
"""This module contans a square class which inherets `Rectangle`"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This class is a rectangle with both dimensions the same (square)"""

    def __init__(self, size):
        """Init function with size being the length of both dimensions"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
