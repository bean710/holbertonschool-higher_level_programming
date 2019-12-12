#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argnum = len(sys.argv)
    # Prints the number, then argument(s) followed by a colon if at least one
    # argument, '.' otherwise
    print("{} ".format(argnum - 1) +
          ("arguments" if argnum != 2 else "argument") +
          ("." if argnum == 1 else ":"))

    for x in range(1, argnum):
        print("{}: {}".format(x, sys.argv[x]))
