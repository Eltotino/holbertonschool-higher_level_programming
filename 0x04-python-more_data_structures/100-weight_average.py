#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        x = y = 0
        for mine in my_list:
            x += mine[0] * mine[1]
            y += mine[1]
            average = x / y
        return average
