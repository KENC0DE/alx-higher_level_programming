#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for ln in row:
                print("{}{}".format(ln, ' ' if ln != row[-1] else ''), end='')
            print("{}".format(''))
