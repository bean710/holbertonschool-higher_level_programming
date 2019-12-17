#!/usr/bin/python3
def multiple_returns(sentence):
    slen = len(sentence)
    fchar = sentence[0] if slen > 0 else None

    return (slen, fchar)
