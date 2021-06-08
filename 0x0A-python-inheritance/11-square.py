#!/usr/bin/python3
"""Module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inherits Rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Builtin for string repr of instance"""
        result = "[Square] {:d}/{:d}".format(self.__size, self.__size)
        return result
