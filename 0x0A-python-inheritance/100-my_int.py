#!/usr/bin/python3
"""
    The Rebelios INT
"""


class MyInt(int):
    """ I am the clawn INT """

    def __eq__(self, val):
        return not super().__eq__(val)

    def __ne__(self, val):
        return not super().__ne__(val)
