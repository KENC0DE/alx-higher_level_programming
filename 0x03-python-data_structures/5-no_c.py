#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    if my_string is not None:
        for c in my_string:
            if c == 'c' or c == 'C':
                new_str += ''
            else:
                new_str += c
        return new_str
