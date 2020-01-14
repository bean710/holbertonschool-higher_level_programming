#!/usr/bin/python3
"""This module is a test-proven paragraph-printer

Tests can be found in `tests/` and can be run using
    `python3 -m doctest ./tests/*`
or
    `python3 -m -v doctest ./tests/*`
for verbose mode.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """The lazy way to multiply two matricies"""
    return np.matmul(m_a, m_b).tolist()
