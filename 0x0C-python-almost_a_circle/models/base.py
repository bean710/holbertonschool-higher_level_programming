#!/usr/bin/python3
"""This module contains a base class for all shape objects"""
import json


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
