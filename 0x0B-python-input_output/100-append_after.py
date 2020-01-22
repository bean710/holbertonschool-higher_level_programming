#!/usr/bin/python3
"""This module contains a function which inserts given text after finding a
string in a line"""


def append_after(filename="", search_string="", new_string=""):
    """Appends `new_string` after every `search_string` is found in a line

    Args:
        filename (str): The name of the file to modify
        search_string (str): The string to search for in each line
        new_string (str): The string to append after each line with
            `search_string` found in it
    """
    with open(filename, "r+") as f:
        contents = f.readlines()
        for line in range(len(contents)):
            if search_string in contents[line]:
                contents.insert(line + 1, new_string)
        f.seek(0)
        f.writelines(contents)
