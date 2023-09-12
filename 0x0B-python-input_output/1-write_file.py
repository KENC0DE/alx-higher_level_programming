#!/usr/bin/python3
"""
    Write into a file
"""


def write_file(filename="", text=""):
    """ writes into a fle func """
    with open(filename, "w", encoding='utf-8') as sf:
        what_written = sf.write(text)
    return what_written
