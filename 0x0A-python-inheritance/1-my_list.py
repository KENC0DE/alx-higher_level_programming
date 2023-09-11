#!/usr/bin/python3
""" class that inherits from List class,
    but modify to print in sorted way
"""


class MyList(list):
    """Inheriting from List class"""

    def print_sorted(self):
        """ sorting method """
        print(sorted(self))
