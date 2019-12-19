#!/usr/bin/python3
def print_sorted_dictionary(d):
    for k, v in {key:d[key] for key in sorted(d.keys())}.items():
        print("{}: {}".format(k, v))
