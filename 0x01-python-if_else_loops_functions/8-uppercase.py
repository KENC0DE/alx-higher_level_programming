#!/usr/bin/python3
def uppercase(str):
    upstr = ''
    for c in str:
        if ord(c) >= ord('a'):
            upstr += chr(ord(c) - 32)
        else:
            upstr += c
    print(upstr)
