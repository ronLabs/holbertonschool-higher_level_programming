#!/usr/bin/python3
"""Base class 1.0"""
import json


class Base:
    """class Base of all classes in project 0x0c"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to convert to json str repr"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
