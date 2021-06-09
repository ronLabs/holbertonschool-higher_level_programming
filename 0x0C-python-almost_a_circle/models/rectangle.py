#!/usr/bin/python3
"""Module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle child class to Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """set value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """get value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Pub method to determine area of rect"""
        return self.__width * self.__height

    def display(self):
        """update the class Rectangle"""
        if (self.y > 0):
            print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """overriding str"""
        a, b, c, d, e = self.id, self.x, self.y, self.width, self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    def update(self, *args, **kwargs):
        """Pub method to assign an arg to each attribute"""
        dict = {
            0: self.id,
            1: self.__width,
            2: self.__height,
            3: self.__x,
            4: self.__y
        }
        if args:
            for counter, value in enumerate(args):
                dict[counter] = value
                self.id, self.__width, self.__height, self.__x, self.__y \
                    = dict[0], dict[1], dict[2], dict[3], dict[4]

        for key, value in kwargs.items():
            if (hasattr(self, key)):
                setattr(self, key, value)

    def to_dictionary(self):
        """Pub method to return dict repr of instances"""
        recDict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return recDict
