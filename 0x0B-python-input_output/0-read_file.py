#!/usr/bin/python3
"""ReadFile module"""


def read_file(filename=""):
    with open(filename, encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
