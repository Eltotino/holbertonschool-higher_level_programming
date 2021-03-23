#!/usr/bin/python3
"""To_Json module"""
import json


def to_json_string(my_obj):
    """Returns Json representation of
    an object

    Args:
        my_obj (object) : given object

    Returns:
        Json (str) : Json representation
    """
    return json.dumps(my_obj)
