#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            if a < x:
                print("{:d}".format(my_list[i], end=""))
                a += 1
        except (ValueError, TypeError):
            i += 1
    print("")
    return a
