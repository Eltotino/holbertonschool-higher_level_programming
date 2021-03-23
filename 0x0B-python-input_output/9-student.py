#!/usr/bin/python3
"""Student Module"""


class Student:
    """Student class

    Attributes:
        first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """Initialises the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves dictionary representation
        of Student instance
        """
        return self.__dict__
