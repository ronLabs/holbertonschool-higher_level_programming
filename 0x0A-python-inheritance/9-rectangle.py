#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Pub Inst Method to determine area"""
        return self.__width * self.__height

    def __str__(self):
        """Builtin for string repr of instance"""
        result = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return result
