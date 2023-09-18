#!/usr/bin/python3
""" 01 Base """


import json
import os


class Base:
    """ Base class (parent) """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        to_save = []
        if list_objs:
            to_save = [ob.to_dictionary() for ob in list_objs]

        fname = cls.__name__ + ".json"
        with open(fname, "w") as j_obj:
            j_obj.write(json.dumps(to_save))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        fname = cls.__name__ + ".json"
        if not os.path.exists(fname):
            return []

        with open(fname, 'r') as jf:
            to_list = jf.read()

        inst_dict = cls.from_json_string(to_list)
        inst = []
        for dic in inst_dict:
            inst.append(cls.create(**dic))

        return inst
