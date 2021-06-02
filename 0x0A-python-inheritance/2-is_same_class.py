#!/usr/bin/python3
"""Module to check object"""


def is_same_class(obj, a_class):
    """function to return True if object is instance of a class"""
    if type(obj) == a_class:
            return True
    else:
        return False
