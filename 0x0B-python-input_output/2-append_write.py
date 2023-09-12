#!/usr/bin/python3
"""
    append to a file
"""


def append_write(filename="", text=""):
    with open(filename, 'a+', encoding='utf-8') as af:
        appended = af.write(text)
    return appended
