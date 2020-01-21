#!/usr/bin/python3
"""This module has a function which reads and outputs an entire file"""


def read_file(filename=""):
    """This function opens a file specified by the argument and prints it to
    standard out"""

    with open(filename) as f:
        print(f.read(), end="")
