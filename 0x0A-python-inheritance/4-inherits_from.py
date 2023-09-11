#!/usr/bin/python3
"""
    is it form that object direcly or indirectly
"""


def inherits_from(obj, a_class):
    """ check if it is inherited dirctly or indirectly"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
