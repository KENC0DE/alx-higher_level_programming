#!/usr/bin/python3
"""
    append to a file
"""


def append_write(filename="", text=""):
    """ appens to a file or create if it doesn't exists """
    with open(filename, 'a+', encoding='utf-8') as af:
        appended = af.write(text)
    return appended
