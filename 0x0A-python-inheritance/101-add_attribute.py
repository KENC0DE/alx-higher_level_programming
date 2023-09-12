#!/usr/bin/python3
"""
    New Attribute
"""


def add_attribute(obj, name, a_name):
    """ add attribute """
    if type(obj) is str:
        raise TypeError("can't add new attribute")
    obj.name = a_name
