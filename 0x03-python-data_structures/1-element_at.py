#!/usr/bin/python3
def element_at(mylist, idx):
    leng = len(mylist)
    if idx < 0 or idx >= leng:
        return None
    else:
        return mylist[idx]
