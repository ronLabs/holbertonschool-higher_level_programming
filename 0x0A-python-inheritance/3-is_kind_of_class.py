#!/usr/bin/python3
"""Module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Function to check object same instance or inherit"""
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
