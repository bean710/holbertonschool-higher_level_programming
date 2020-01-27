#!/usr/bin/python3
"""This module contains a base class for all shape objects"""
import json
import turtle
import random as rand


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of the list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]" or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of object to a file"""
        if list_objs is None:
            ld = []
        else:
            ld = [d.to_dictionary() for d in list_objs]

        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(Base.to_json_string(ld))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of `cls` using the elements of `dictionary`"""
        b1 = cls(2, 2)
        b1.update(**dictionary)
        return b1

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the rectangles and squares using turtles"""
        turt = turtle.Turtle()
        colormode = turt.getscreen().colormode()

        for rect in list_rectangles:
            color = (rand.random() * colormode,
                          rand.random() * colormode,
                          rand.random() * colormode)
            turt.color(color, color)
            turt.begin_fill()
            turt.setposition(rect.x, rect.y)
            turt.pendown()
            turt.forward(rect.width)
            turt.right(90)
            turt.forward(rect.height)
            turt.right(90)
            turt.forward(rect.width)
            turt.right(90)
            turt.forward(rect.height)
            turt.right(90)
            turt.end_fill()
            turt.color("black", "black")
            turt.penup()
            turt.setpos(rect.x + rect.width / 2, rect.y - rect.height / 2)
            turt.write(rect.id)

        for square in list_squares:
            color = (rand.random() * colormode,
                     rand.random() * colormode,
                     rand.random() * colormode)
            turt.color(color, color)
            turt.setposition(square.x, square.y)
            turt.pendown()
            for x in range(4):
                turt.forward(square.size)
                turt.right(90)
            turt.penup()

        turtle.done()

    @classmethod
    def load_from_file(cls):
        """Loads a list of class instances from a file"""
        ret = []
        with open(cls.__name__ + ".json", "r") as f:
            li = cls.from_json_string(f.read())
            for di in li:
                ret.append(cls.create(**di))

        return ret
