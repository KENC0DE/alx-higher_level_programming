#!/usr/bin/python3
def roman_to_int(rm):
    if not isinstance(rm, str) or rm is None:
        return None
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    leng = len(rm)
    flag = 1
    for n in range(leng):
        if n + 1 < leng:
            if rome.get(rm[n]) < rome.get(rm[n + 1]):
                num += rome.get(rm[n + 1]) - rome.get(rm[n])
                flag = 0
            else:
                num += rome.get(rm[n])
                flag = 1
        elif flag:
            num += rome.get(rm[n])
    return num
