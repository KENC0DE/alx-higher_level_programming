#!/usr/bin/python3
"""
    Is it the same class???
"""


def is_same_class(obj, a_class):
    """ check if they are the same class"""

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    return False
