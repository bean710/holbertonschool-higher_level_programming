#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for element in my_list:
        if num >= x:
            break

        try:
            print("{:d}".format(element), end="")
        except:
            continue
        else:
            num += 1

    print("")
    return num
