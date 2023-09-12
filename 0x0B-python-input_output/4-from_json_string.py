#!/usr/bin/python3
"""
    from json to python object
"""


import json


def from_json_string(str):
    """to python data"""
    return json.loads(str)
