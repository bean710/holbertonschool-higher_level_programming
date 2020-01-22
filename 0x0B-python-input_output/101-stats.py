#!/usr/bin/python3
"""This script reads and reports on data from stdin"""
import sys


if __name__ == "__main__":
    lnum = 0
    codes = {}
    fsize = 0
    try:
        for line in sys.stdin:
            sep = line.split(" ")

            fsize += int(sep[-1])

            if sep[-2] not in codes:
                codes[sep[-2]] = 1
            else:
                codes[sep[-2]] += 1

            lnum += 1
            if line is None or lnum % 10 == 0:
                print("File size: {}".format(fsize))
                for k in sorted(codes):
                    print("{}: {}".format(k, codes[k]))

    except (KeyboardInterrupt, SystemExit):
        print("File size: {}".format(fsize))
        for k in sorted(codes):
            print("{}: {}".format(k, codes[k]))
