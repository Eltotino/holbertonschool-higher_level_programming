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

    no_space = True
    for c in range(len(text)):
        if text[c] == ' ' and no_space:
            continue
        else:
            if text[c] in ":.?":
                print(text[c], end="\n\n")
                no_space = True
            else:
                print(text[c], end='')
                no_space = False
