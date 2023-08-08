#!/usr/bin/python3
def uppercase(str):
    if str == "":
        return

    for c in range(len(str) - 1):
        if ord(str[c]) <= ord('Z'):
            top = str[c]
        else:
            top = chr(ord(str[c]) - 32)
        print("{}".format(top), end='')

    if ord(str[c + 1]) <= ord('Z'):
        top = str[c + 1]
    else:
        top = chr(ord(str[c + 1]) - 32)

    print("{}".format(top))
