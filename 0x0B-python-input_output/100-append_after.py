#!/usr/bin/python3
"""AppendAfter module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of a text file, after each line containing a specefic
        string"""
    with open(filename, "r+", encoding="utf-8") as file:
        string = ""
        for line in file:
            string += line
            if search_string in line:
                string += new_string
        file.seek(0)
        file.write(string)
