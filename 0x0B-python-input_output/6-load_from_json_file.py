#!/usr/bin/python3
"""
    create an object from json
"""


import json


def load_from_json_file(filename):
    """ create object from json """
    with open(filename, "r") as mko:
        obj = json.loads(mko.read())
    return obj
