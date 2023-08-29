#!/usr/bin/python3
"""Class with prinvate attribut and pre-check assignment"""


class Square:
    """Initializer"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """ private value returner """
    def area(self):
        return self.__size ** 2
