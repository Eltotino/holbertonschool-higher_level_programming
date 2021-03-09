#!/usr/bin/python3
"""Same class Module"""


def is_same_class(obj, a_class):
    """Says if the object is exactly
    an instance of the class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
