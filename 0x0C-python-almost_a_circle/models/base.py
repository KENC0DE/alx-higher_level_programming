#!/usr/bin/python3
""" 01 Base """


class Base:
    """ Base class (parent) """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
