#!/usr/bin/python3
"""
    Add attribute
"""


def add_attribute(obj, name, a_name):
    """
        add attribute
    """

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, name):
        raise TypeError("can't add new attribute")

    setattr(obj, name, a_name)
