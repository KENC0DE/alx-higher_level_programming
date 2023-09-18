#!/usr/bin/python3
"""
    Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square is Just a special Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    # ///// setter and getter //////
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        sarg = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                args + sarg[len(args):]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
