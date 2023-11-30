#!/usr/bin/python3
"""
    Search Peak:
"""


def find_peak(lfi):
    """ Return peak value from unsorted passed integers
    """
    if not lfi or lfi == []:
        return None
    lf, rt = 0, len(lfi) - 1
    while lf < rt:
        mid = (lf + rt) // 2
        if lfi[mid] >= lfi[mid + 1]:
            rt = mid
        else:
            lf = mid + 1
    return lfi[lf]
