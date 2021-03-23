#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """Appends a text to a given file and 
    returns the number of added characters

    Args:
        filename(str): file name
        text(str): a given text
    """
    with open(filename, mode='a', encoding="UTF-8") as my_file:
        my_file.write(text)

    with open(filename, encoding="UTF-8") as my_file:

        count = 0
        for word in my_file:
            for char in word:
                count += 1

    return len(word)
    