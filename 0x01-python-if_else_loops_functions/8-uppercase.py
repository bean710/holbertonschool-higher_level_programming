#!/usr/bin/python3
def islower(c):
    o = ord(c)
    if (o >= 97 and o <= 122):
        return True
    return False

def toupper(c):
    if (islower(c)):
        return chr(ord(c) - 32)
    return (c)

def uppercase(str):
    for c in range(len(str)):
        if (c == len(str) - 1):
            print("{}".format(toupper(str[c])))
        else:
            print("{}".format(toupper(str[c])), end="")
