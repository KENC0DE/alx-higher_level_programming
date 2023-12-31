#!/usr/bin/python3
""" Rectangle """


Base = __import__('7-base_geometry').BaseGeometry


class Rectangle(Base):
    """ Inheritor class """

    def __init__(self, width, height):
        """ initializor. """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
