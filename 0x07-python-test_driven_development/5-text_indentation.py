#!/usr/bin/python3
""" TextIndentaion module """


def text_indentation(text):
    """
    Prints a text with 2 new lines after :'.' , '?' , ':'
    Args:
        text (str): string
    Raises:
        TypeError: argument passed is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    strg = ""
    for char in text:
        strg += char
        if char in ":.?":
            print(strg.lstrip(), end="\n\n")
            strg = ""
    print(strg.lstrip(), end='')
