#!/usr/bin/python3
"""Class with prinvate attribut and pre-check assignment"""


class Square:
    """Initializer"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        return self.__position

    @position.setter
    def position(self, val):
        if type(val) is not tuple or len(val) != 2 or \
           type(val[0]) is not int or val[0] < 0 or \
           type(val[1]) is not int or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = val

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for sy in range(self.__position[1]):
            print()
        for sq in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)

    def __str__(self):
        sqr = []
        sqr.append("\n" * (self.__position[1] - 1))
        for sq in range(self.__size):
            sqr.append((" " * self.__position[0]) + ("#" * self.__size))
        return ("\n".join(sqr))
