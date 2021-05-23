#!/usr/bin/python3
"""Create class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square"""
        self.__size = size
        self.position = position
        """if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")"""

    def area(self, area=0):
        """defines area"""
        return(self.__size * self.__size)

    @property
    def size(self):

        """ define size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define area"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print Square"""
        if self.__size:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.__size))
        else:
            print()

    @property
    def position(self):

        """ position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
