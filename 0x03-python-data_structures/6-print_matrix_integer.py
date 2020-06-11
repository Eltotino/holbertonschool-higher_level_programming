#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        s = ''
        for j in i:
            s += str(j) + " "
        print(s[0:-1])
