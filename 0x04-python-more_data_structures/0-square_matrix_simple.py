#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    for mtrx_row in matrix:
        mtrx_row = list(map(lambda x: x**2, row))
        sqr_mtx.append(mtrx_row)
    return sqr_mtx
