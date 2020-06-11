#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = ''
        for j in i:
            l += str(j) + " "
        print(l[0:-1])
