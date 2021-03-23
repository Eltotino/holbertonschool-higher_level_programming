#!/usr/bin/python3
"""Write File module"""


def write_file(filename="", text=""):
    """Writes a string into a file and
    returns number of lines in a txt file

    Args:
        filename(str): file name
        text(str): a given text
    """
    with open(filename, mode='w', encoding="UTF-8") as my_file:
        my_file.write(text)

    with open(filename, encoding="UTF-8") as my_file:

        count = 0
        for word in my_file:
            for char in word:
                count += 1

    return count
