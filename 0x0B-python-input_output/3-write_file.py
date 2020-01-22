#!/usr/bin/python3
"""This module contains a function which writes given text to a given file"""


def write_file(filename="", text=""):
    """Writes `text` to `filename`

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file
    """
    with open(filename, "w") as f:
        f.write(text)
