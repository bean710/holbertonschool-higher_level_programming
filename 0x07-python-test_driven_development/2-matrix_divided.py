#!/usr/bin/python3
"""This module is a test-proven matrix multiplier

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""


def matrix_divided(matrix, div):
    """Divides an entire matrix by a constant number

    Args:
        matrix: The matrix to divide each item of
        div: The number to divide each element by

    Returns:
        A new matrix with each element divided by ``div``
    """
    if not isinstance(matrix, list) or matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    ret = [row[:] for row in matrix]
    for l in range(len(ret)):
        if not isinstance(ret[l], list):
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")

        if len(ret[l]) is not len(ret[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for i in range(len(ret[l])):
            if not isinstance(ret[l][i], (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

            ret[l][i] = round(ret[l][i] / div, 2)

    return ret
