#!/usr/bin/python3
def safe_print_integer(value):
    istf = True
    try:
        print("{:d}".format(value))
    except ValueError:
        istf = False
    return istf
