#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initailazer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the json representation of instance"""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Reloads form json"""
        for key, value in json.items():
            self.__dict__[key] = value
