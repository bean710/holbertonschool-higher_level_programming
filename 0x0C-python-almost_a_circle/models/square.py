"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is based of rectangle, but both dimensions are equal"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints a nice version of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size (width, height) of the square"""
        self.update(width=value, height=value)
