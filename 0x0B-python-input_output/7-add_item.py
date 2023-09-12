#!/usr/bin/python3
"""
    make argument to JSON
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def arg_to_list(f_name):
    """ Configure JSON """
    obj_form = load_from_json_file(f_name)
    save_to_json_file(obj_form, f_name)


def main():
    """ execution point """
    if sys.argv is None:
        return
    f_name = "add_item.json"
    save_to_json_file(sys.argv[1:], f_name)
    arg_to_list(f_name)


main()
