#!/usr/bin/python3
"""Same class Module"""


def is_same_class(obj, a_class):
    """Says if the object is exactly
    an instance of the class

    Args: 
        obj: the object
        a_class: the class

    Returns:
        True if obj is instance of a_class
        False if otherwise
    """
    return type(obj)== a_class

