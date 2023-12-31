#!/usr/bin/python3
""" 01 Base """
import json
import os
import csv
import turtle


class Base:
    """ Base class (parent) """

    __nb_objects = 0

    def __init__(self, id=None):
        """ doc """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ doc """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ doc """
        to_save = []
        if list_objs:
            to_save = [ob.to_dictionary() for ob in list_objs]

        fname = cls.__name__ + ".json"
        with open(fname, "w") as j_obj:
            j_obj.write(cls.to_json_string(to_save))

    @staticmethod
    def from_json_string(json_string):
        """ doc """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ doc """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ doc """
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ doc """
        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ doc """
        filename = cls.__name__ + ".csv"
        lst = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        lst.append(i)
        return lst

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """ doc """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
