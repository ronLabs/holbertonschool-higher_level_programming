#!/usr/bin/python3
"""Module of real definition of a rectangle"""


class Rectangle():
    """class Rectangle defined with priv inst attrib width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """method to get value of width"""
        return self.__width

    @property
    def height(self):
        """method to get value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """method to set the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """method to set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """publ ins method to determine area of rect"""
        ar = self.__width * self.__height
        return ar

    def perimeter(self):
        """publ inst method to determine perimeter of rect"""
        per = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            per = 0
        return per

    def __str__(self):
        """built in to return printed representation of string instance"""
        fig = ""
        if self.__height == 0 or self.__width == 0:
                    return fig
        for i in range(self.__height):
            for j in range(self.__width):
                fig += str(self.print_symbol)
            fig += '\n'
        return fig[:-1]

    def __repr__(self):
        """Built in method to return string representation of rect"""
        return "Rectangle({}, {})".format(eval(repr(self.__width)), (
                eval(repr(self.__height))))

    def __del__(self):
        """Builtin to ensure proper deletion of instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static metho to return bigger instance"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area()) == (rect_2.area()):
                return rect_1
            elif (rect_1.area()) > (rect_2.area()):
                return rect_1
            elif (rect_1.area()) < (rect_2.area()):
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new rectangle"""
        return cls(size, size)
