#!/usr/bin/python3
"""This module contains a class that inherits `list` and adds a function to
print the list sorted in ascending order"""


class MyList(list):
    """Special list class with a sorted-print function"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""

        print(sorted(self))
