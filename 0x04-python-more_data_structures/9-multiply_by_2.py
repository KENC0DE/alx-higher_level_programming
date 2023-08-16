#!/usr/bin/python3
def multiply_by_2(a_dic):
    nw_dic = {}
    for v in a_dic:
        nw_dic[v] = a_dic[v] * 2
    return nw_dic
