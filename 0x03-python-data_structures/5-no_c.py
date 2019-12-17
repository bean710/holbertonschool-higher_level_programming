#!/usr/bin/python3
def no_c(my_strin):
    ret = ""
    for c in my_strin:
        if not (c == "c" or c == "C"):
            ret = ret + c
    return ret
