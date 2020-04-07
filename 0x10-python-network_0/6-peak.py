#!/usr/bin/python3
"""This program finds a peak in a dataset"""


def find_peak(list_of_integers):
    """Recursive peak-finding function"""
    loi = list_of_integers
    if loi is None or len(loi) == 0:
        return None

    if (len(loi) == 1):
        return (loi[0])

    mid = len(loi) // 2
    if (loi[mid - 1] > loi[mid]):
        return(find_peak(loi[:mid]))
    elif (loi[mid + 1] > loi[mid]):
        return(find_peak(loi[mid + 1:]))
    else:
        return(loi[mid])
