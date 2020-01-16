#!/usr/bin/python3
"""Module contains a class which prevents attributes from being added"""


class LockedClass:
    """Specially locked class"""
    def __setattr__(self, key, value):
        """Overriding the set attribute function to only allow certian keys"""
        if key != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 str(key) + "'")
        super().__setattr__(key, value)
