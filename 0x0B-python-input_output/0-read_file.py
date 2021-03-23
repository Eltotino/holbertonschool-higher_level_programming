#!/usr/bin/python3
"""ReadFile module"""


def read_file(filename=""):
    """Reads a text file and print inin stdout

    Args:
        filename (str): the file that needs to be opened
    """

    with open(filename, encoding="UTF-8") as my_file:
        file = my_file.read()
        print(file, end="")
