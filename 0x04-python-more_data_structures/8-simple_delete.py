#!/usr/bin/python3
def simple_delete(a_dic, key=""):
    if a_dic.get(key) is not None:
        del a_dic[key]
    return a_dic
