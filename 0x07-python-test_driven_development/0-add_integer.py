#!/usr/bin/python3
"""Add_integer module"""


def add_integer(a, b=98):
    """Args:va : integer, b : integer

    Returns: (int) : addition of a  and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    return int(a + b)
