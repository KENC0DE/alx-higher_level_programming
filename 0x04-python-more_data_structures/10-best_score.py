#!/usr/bin/python3
def best_score(a_dic):
    if a_dic is not None:
        scr = 0
        track = 0
        for c in a_dic:
            scr = scr if scr > a_dic[c] else a_dic[c]
            if track != scr:
                name = c
                track = scr
        return name

    return None
