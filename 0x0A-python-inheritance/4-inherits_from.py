#!/usr/bin/python3
"""Module for function inherits_from"""


def inherits_from(obj, a_class):
    """function check obj inherited from a specified class"""
    obType = type(obj)
    if issubclass(obType, a_class):
        return True
    else:
        return False
