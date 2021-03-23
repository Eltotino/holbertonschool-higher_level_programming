#!/usr/bin/python3
"""Json_to_string module"""
import json


def from_json_string(my_str):
    """Returns an object represented by a Json
    string

    Args:
        my_str (str) : given object

    Returns:
        Json (obj) : Json string
    """
    return json.loads(my_str)
