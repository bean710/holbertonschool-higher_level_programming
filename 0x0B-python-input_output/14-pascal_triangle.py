#!/usr/bin/python3
"""This module contains a function which generates a pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists representing pascal's triangle of size `n`"""

    if n <= 0:
        return []

    return pascal_recur(n, [[1]])


def pascal_recur(n, l):
    """Recursive function used for calculating pascal's triangle"""

    if n == 1:
        return l
    row = []
    for x in range(len(l[-1]) + 1):
        row.append((l[-1][x - 1] if x - 1 >= 0 else 0) +
                   (l[-1][x] if x < len(l[-1]) else 0))
    l.append(row)
    return pascal_recur(n - 1, l)
