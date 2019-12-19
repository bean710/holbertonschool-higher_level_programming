#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = list(map(list, matrix))
    for i in range(len(new_mat)):
        for j in range(len(new_mat[i])):
            new_mat[i][j] = matrix[i][j] * matrix[i][j]

    return new_mat
