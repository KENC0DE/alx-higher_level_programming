#!/usr/bin/python3
def best_score(a_dic):
    if a_dic == {}:
        return None
    if a_dic is not None:
        name = next(iter(a_dic))
        scr = a_dic.get(name)
        for c in a_dic:
            if scr < a_dic[c]:
                name = c
                scr = a_dic[c]
        return name

    return None
