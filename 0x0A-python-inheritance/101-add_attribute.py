#!/usr/bin/python3
"""
    New Attribute
"""


def add_attribute(obj, name, a_name):
    """ add attribute """

    bltc = (int, float, tuple, str, frozenset,
            bytes, complex, bool, None.__class__)

    if any((isinstance(obj, blt) for blt in bltc)):
        raise TypeError("can't add new attribute")
    obj.name = a_name
