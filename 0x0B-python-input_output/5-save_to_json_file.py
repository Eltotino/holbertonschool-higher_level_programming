#!/usr/bin/python3
"""SaveToJsonFile module"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object into a Json file

    Args:
        filename(str) :  a file
        my_obj(obj): given object

    """
    with open(filename, 'w', encoding="utf_8") as file:
        json.dump(my_obj, file)
