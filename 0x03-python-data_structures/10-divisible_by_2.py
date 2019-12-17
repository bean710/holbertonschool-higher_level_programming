#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = []
    for x in my_list:
        ret = ret + ([True] if not x % 2 else [False])

    return ret
