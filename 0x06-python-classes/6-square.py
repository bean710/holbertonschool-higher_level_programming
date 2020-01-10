#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        if (not all(x >= 0 and type(x) is int for x in value)
                or len(value) is not 2 or type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for x in range(self.position[1]):
                print("")
            for x in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
