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

    def to_json(self):
        return self.__dict__
