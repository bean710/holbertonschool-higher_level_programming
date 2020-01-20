#!/usr/bin/python3
"""This module contains a special int class"""


class MyInt(int):
    """Int class that has backwards equality comparison"""

    def __eq__(self, other): 
        """Function to invert the == comparison"""

        return self != other
