#!/usr/bin/python3
"""This module contains a function which returns a class' dictionary as a JSON
serializable object"""


def class_to_json(obj):
    """Converts `obj`s dictionary to a JSON serializable object

    Args:
        obj (class): The python class which dictionary is to be converted to a
            JSON object

    Returns:
        str: `obj`s dictionary as a JSON serializable object
    """
    return obj.__dict__
