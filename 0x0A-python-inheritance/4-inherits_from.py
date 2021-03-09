#!/usr/bin/python3
"""Kind of a class Module"""


def inherits_from(obj, a_class):
    """Says if the object is an instance of a
    class that inherited from specified class

    Args:
        obj: the object
        a_class : the class

    Returns:
        True if is a subclass
        False if otherwise
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
         return False
