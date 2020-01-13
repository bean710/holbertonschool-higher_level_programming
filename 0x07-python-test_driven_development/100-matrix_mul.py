#!/usr/bin/python3
"""This module is a test-proven paragraph-printer

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""

def matrix_mul(m_a, m_b):
    """Matrix multiplication function

    Args:
        m_a: The first matrix
        m_b: The second matrix

    Returns:
        m_a * m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(x) is list for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(x) is list for x in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(all(type(y) in [float, int] for y in x) for x in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(type(y) in [float, int] for y in x) for x in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(x) == len(m_a[0]) for x in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(x) == len(m_b[0]) for x in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    ret = []
    for x in range(len(m_a)):
        nl = []
        for y in range(len(m_b[0])):
            tmp = 0;
            for z in range(len(m_a[0])):
                tmp += m_a[x][z] * m_b[z][y]
            nl.append(tmp)
        ret.append(nl)

    return ret
