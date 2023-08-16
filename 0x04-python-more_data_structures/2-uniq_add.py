#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp_check = []
    unique_add = 0
    for n in my_list:
        if n not in tmp_check:
            unique_add += n
            tmp_check.append(n)
    return unique_add
