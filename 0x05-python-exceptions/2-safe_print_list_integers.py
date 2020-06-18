#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    i = 0
    while i < x:
        try:
            if a == int(a):
                print("{:d}".format(my_list[i]), end="")
                i += 1
        except (ValueError, TypeError):
            i += 1
    print("")
    return i
