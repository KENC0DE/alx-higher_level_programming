#!/usr/bin/python3
"""Class with prinvate attribut and pre-check assignment"""


class Square:
    """Initializer"""
    def __init__(self, size=0, pst=(0, 0)):
        self.__size = size
        self.__pst = pst

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Do Nothing """
        pass

    @position.setter
    def position(self, val):
        if (type(val) is not tuple or
                len(val) != 2 or
                type(val[0]) is not int or
                type(val[1]) is not int or
                val[0] < 0 or
                val[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__pst = val

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for sy in range(self.__pst[1]):
            print()
        for sq in range(self.__size):
            print(" " * self.__pst[0], end='')
            print("#" * self.__size)
