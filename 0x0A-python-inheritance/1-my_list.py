#!/usr/bin/python3
"""Mylist Module"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
