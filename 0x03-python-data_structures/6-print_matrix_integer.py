#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return

    for x in matrix:
        for y in range(len(x)):
            print("{:d}".format(x[y]), end=("\n" if y == len(x) - 1 else " "))
