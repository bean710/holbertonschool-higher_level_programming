#!/usr/bin/python3
"""This module contains a class with a JSON serialization function"""


class Student:
    """Basic student class to demonstrate serialization"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the student to a dictionary for serialization

        Args:
            attrs (:obj:`list` of :obj:`str`): List of attributes to retrieve

        Returns:
            :obj:`dict`: A dictionary version of the Student's attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Loads Student attributes from dictionary

        Args:
            json: The dictionary to load data from
        """
        self.__dict__.update(json)
