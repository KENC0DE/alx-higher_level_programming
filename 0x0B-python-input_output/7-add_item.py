#!/usr/bin/python3
"""
    make argument to JSON
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def arg_to_list():
    """ Configure JSON """
    f_name = "add_item.json"
    save_to_json_file(sys.argv[1:], f_name)


arg_to_list()
