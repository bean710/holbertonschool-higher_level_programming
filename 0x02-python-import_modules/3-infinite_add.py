#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argnum = len(sys.argv)
    count = 0

    for x in range(1, argnum):
        count += int(sys.argv[x])

    print(count)
