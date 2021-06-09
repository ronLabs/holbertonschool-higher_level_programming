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

    def update(self, *args, **kwargs):
        """Pub method to assign and update attributes"""
        sdict = {
            0: self.id,
            1: self.size,
            2: self.x,
            3: self.y,
        }

        for counter, value in enumerate(args):
            sdict[counter] = value
            self.id, self.size, self.x, self.y = \
                sdict[0], sdict[1], sdict[2], sdict[3]

        for key, value in kwargs.items():
            if (hasattr(self, key)):
                setattr(self, key, value)

        def to_dictionary(self):
        """Pub method to print str repr of sqr"""
        sqDict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return sqDict
