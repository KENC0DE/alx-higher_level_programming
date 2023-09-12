#!/usr/bin/python3
"""
    make argument to JSON
"""


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def arg_to_list():
    """ Configure JSON """
    f_name = "add_item.json"
    ob_f = []
    if os.path.exists(f_name):
        ob_f = load_from_json_file(f_name)

    ob_in = sys.argv[1:]
    obj = ob_f + ob_in
    save_to_json_file(obj, f_name)


arg_to_list()
