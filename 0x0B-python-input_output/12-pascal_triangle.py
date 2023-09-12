#!/usr/bin/python3
"""
    make triangle
"""


def pascal_triangle(n):
    """ Creates pascal triangle """
    p_triangle = [[1], [1, 1]]
    cr = 1
    if n <= 0:
        return p_triangle
    if n == 1:
        return p_triangle[:-1]
    for i in range(2, n):
        tp = p_triangle[cr]
        cr += 1

        tmp_ls = [1]
        for j in range(len(tp)):
            if j + 1 < len(tp):
                tmp_ls.append(tp[j] + tp[j + 1])
            else:
                tmp_ls.append(1)
                p_triangle.append(tmp_ls)
                break
    return p_triangle
