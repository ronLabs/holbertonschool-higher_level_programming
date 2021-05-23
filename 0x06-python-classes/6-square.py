#!/usr/bin/python3
""""Module of updated Square with getter and setter"""


class Square():
    """Square class with private instance attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Public Method for area of square"""
    def area(self):
        ar = self.__size ** 2
        return ar

    """Public Method prints a square"""
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.__size))

    @property
    def size(self):
        """method to get value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set value of size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        elif not isinstance(value, int):
                raise TypeError("size must be an integer")
    @property
    def position(self):
        """method to get value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """method to set value of position"""
        if not isinstance(value, tuple) and value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
