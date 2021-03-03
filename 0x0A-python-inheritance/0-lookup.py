#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """
    Function that returns list of available attribute and method
    of an object.

    Args: obj: object

    Returns: list of attribute and methods of said object
    """
    return dir(obj)
