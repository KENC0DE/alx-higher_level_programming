#!/usr/bin/python3
"""
    write json into a file
"""


import json


def save_to_json_file(obj, fname):
    """ write obj to f name """
    with open(fname, "w") as jf:
        jf.write(json.dumps(obj))
