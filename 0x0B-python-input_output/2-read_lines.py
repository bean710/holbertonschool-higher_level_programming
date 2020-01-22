"""This module contains a function which prints a given number of lines from a
given file"""


def read_lines(filename="", nb_lines=0):
    """Prints `nb_lines` from file `filename`

    Args:
        filename (str): The name of the file to read from
        nb_lines (int): The number of lines to print
    """
    with open(filename) as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        else:
            for line, n in zip(f, range(nb_lines)):
                print(line, end="")
