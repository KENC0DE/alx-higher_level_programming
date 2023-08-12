#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for ln in row:
                print("{:d}".format(ln), end=' ' if ln != row[-1] else '')
            print("{}".format(''))
