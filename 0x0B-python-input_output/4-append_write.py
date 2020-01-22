#!/usr/bin/python3
"""This module contains a function which appends given text to a given file"""


def write_file(filename="", text=""):
    """Appends `text` to `filename`

    Args:
        filename (str): The name of the file to write to
        text (str): The text to append to the file
    """
    with open(filename, "a") as f:
        return f.write(text)
