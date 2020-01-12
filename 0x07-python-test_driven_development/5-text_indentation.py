#!/usr/bin/python3
"""This module is a test-proven paragraph-printer

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""


def text_indentation(text):
    """Prints a string with style

    This function adds two newlines after each '.', '?', and ':'.
    It also removes any whitespace before and after each "sentance"

    Args:
        text (str): The text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    if text is "":
        print("")
        return

    last = 0
    fin = []
    for c in range(len(text)):
        if text[c] is "." or text[c] is "?" or text[c] is ":":
            fin.append(text[last:c + 1])
            last = c + 1

    if last < c - 1:
        fin.append(text[last:c + 1])

    for item in range(len(fin)):
        fin[item] = fin[item].strip()

    for item in fin:
        if item is not "":
            print(item)
            print("")
        elif len(fin) is 1:
            print("")
