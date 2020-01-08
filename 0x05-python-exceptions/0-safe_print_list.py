#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for element in my_list:
        if num >= x:
            break
        try:
            print(element, end="")
        except:
            break
        else:
            num += 1

    print("")
    return num
