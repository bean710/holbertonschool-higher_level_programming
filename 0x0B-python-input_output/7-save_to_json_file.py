#!/usr/bin/python3
"""This module contains a function which saves a python object to a file in
its JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Saves `my_obj` to `filename` as JSON

    Args:
        my_obj: The python object to be saved
        filename (str): The name of the file to save the object to
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
