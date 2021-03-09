#!/usr/bin/python3
"""Kind of a class Module"""


def is_kind_of_class(obj, a_class):
    """Says if the object is an instance of a
    class or from a class that inherited from the
    specified class

    Args:
        obj: the object
        a_class : the class

    Returns:
        True if is an instance of the given class
        from a class that inherited from the
        specified class
        False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
