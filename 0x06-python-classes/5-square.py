#!/usr/bin/python3
""""Module of updated Square with getter and setter"""


class Square():
    """Square class with private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size

    """Public Method for area of square"""
    def area(self):
        ar = self.__size ** 2
        return ar

    """Public Method prints a square"""
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format("#"), end="")
                print()

    @property
    def size(self):
        """method to get value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
