#!/usr/bin/python3
"""
    BASE ON > ON
"""


class BaseGeometry:
    """ Geometry building ... """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validator """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
