#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    alen = len(tuple_a)
    blen = len(tuple_b)
    f = (tuple_a[0] if alen >= 1 else 0) + (tuple_b[0] if blen >= 1 else 0)

    s = (tuple_a[1] if alen >= 2 else 0) + (tuple_b[1] if blen >= 2 else 0)

    ret = (f, s)

    return ret
