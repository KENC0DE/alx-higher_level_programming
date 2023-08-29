#!/usr/bin/python3
"""Class with prinvate attribut and pre-check assignment"""


class Square:
    """Initializer"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for sq in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
        else:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
