#!/usr/bin/python3
def element_at(my_list, idx):
    for elt in my_list:
        if idx < 0:
            return("None")
        elif idx > len(my_list):
            return("None")
        else:
            return(idx + 1)