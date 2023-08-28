#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as expt:
        print("Exception:", expt, file=sys.stderr)
        return None
