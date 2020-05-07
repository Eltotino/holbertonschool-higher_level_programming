#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list =[]
    for i in matrix:
        new_list.append(list(j ** 2 for j in i))
    return new_list
