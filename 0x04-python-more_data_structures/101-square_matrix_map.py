#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    nmat = []
    for row in matrix:
        nmat.append(list(map(lambda x: x ** 2, row)))

    return nmat
