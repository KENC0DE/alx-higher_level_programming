#!/usr/bin/python3
"""
    Read from a file
"""


def read_file(filename=""):
    """ Read file """
    with open(filename, 'r', encoding='utf-8') as fp:
        print(fp.read(), end='')
