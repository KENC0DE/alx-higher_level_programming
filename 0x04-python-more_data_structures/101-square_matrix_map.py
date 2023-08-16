#!/usr/bin/python3
def square_matrix_map(mtrx=[]):
    return [list(map(lambda x: x * x, row)) for row in mtrx]
