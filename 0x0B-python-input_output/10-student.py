#!/usr/bin/python3
"""
    Play with student
"""


class Student:
    """ Student class """

    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def to_json(self, attrs=None):
        fdi = self.__dict__
        if attrs is None:
            return fdi
        emp = {x: fdi[x] for x in attrs if x in fdi}
        return emp
