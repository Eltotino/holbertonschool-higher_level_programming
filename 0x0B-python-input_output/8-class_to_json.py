#!/usr/bin/python3
"""Class to json module"""


def class_to_json(obj):
    """Gives a dictionary description
    with simple data structure

    Args:
        obj(obj): given object

    Returns:
        a dictionary with simple data structure
    """
    return obj.__str__
