#!/usr/bin/python3
"""Add attributes module"""


def add_attribute(obj, key, value):
    """Adds attributes to the given object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
