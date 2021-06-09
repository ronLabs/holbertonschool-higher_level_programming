#!/usr/bin/python3
"""Module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """builtin to print string repr of instance"""
        result = "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                 self.id, self.x, self.y, self.size)
        return result
