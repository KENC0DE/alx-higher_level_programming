#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for x in my_list:
        res.append(1 if x % 2 == 0 else 0)
    return res
