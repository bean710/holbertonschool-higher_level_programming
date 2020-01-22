#!/usr/bin/python3
"""This module contains a function which converts a JSON string to a python
object"""
import json


def from_json_string(my_str):
    """Converts `my_str` to a python object

    Args:
        my_str: The JSON string to be converted

    Returns:
        obj: A python object version of the JSON string
    """
    return json.loads(my_str)
