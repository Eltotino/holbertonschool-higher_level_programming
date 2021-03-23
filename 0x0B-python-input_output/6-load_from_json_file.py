#!/usr/bin/python3
"""LoadFromJsonFile module"""
import json


def load_from_json_file(filename):
    """Creates an object from Json file

    Args:
        filename(obj): name of a file

    """
    with open(filename, 'r', encoding="UTF-8") as my_file:
        return json.load(my_file)
