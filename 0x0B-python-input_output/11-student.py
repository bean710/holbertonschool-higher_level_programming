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

    def to_json(self):
        """Converts the student to a dictionary for serialization

        Returns:
            obj: A serializable python object version of the Student
        """
        return self.__dict__
