#!/usr/bin/python3
def raise_exception_msg(msg=""):
    try:
        raise TypeError
    except TypeError:
        print(msg)
