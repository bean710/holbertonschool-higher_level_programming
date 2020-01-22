#!/usr/bin/python3
"""This module contains a function which JSON serializes Python objects"""
import json


def to_json_string(my_obj):
    """Converts `my_obj` to a JSON string

    Args:
        my_obj: The object to be converted

    Returns:
        str: The JSON version of the object as a string
    """
    return json.dumps(my_obj)
