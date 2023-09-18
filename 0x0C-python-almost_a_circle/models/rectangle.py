#!/usr/bin/python3
"""
    Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Define Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializer """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args, **kwargs):
        sarg = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                args + sarg[len(args):]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dic = {'x': self.__x, 'y': self.__y,
               'id': self.id, 'height': self.__height,
               'width': self.__width}
        return dic
