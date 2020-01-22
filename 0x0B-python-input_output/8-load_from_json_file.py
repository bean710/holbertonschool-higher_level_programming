#!/usr/bin/python3
"""This module contains a function which loads a python object from JSON in a
given file"""
import json


def load_from_json_file(filename):
    """Loads a python object from JSON in `filename`

    Args:
        filename (str): The name of the file to load the object from

    Returns:
        obj: The python object loaded from the JSON
    """
    with open(filename) as f:
        return json.loads(f.read())
