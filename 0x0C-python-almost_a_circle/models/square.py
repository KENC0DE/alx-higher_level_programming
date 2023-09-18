#!/usr/bin/python3
"""
    Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square is Just a special Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ doc """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ doc """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    # ///// setter and getter //////
    @property
    def size(self):
        """ doc """
        return self.width

    @size.setter
    def size(self, val):
        """ doc """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ doc """
        sarg = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                args + sarg[len(args):]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ doc """
        dic = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dic
