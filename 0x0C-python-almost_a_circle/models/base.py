#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialiser of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns Json representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write Json representation of string"""
        lista = []
        if list_objs is not None:
            for dic in list_objs:
                lista.append(cls.to_dictionary(dic))
        with open(str(cls.__name__ + ".json"), "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """ returns Json representation's list"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)
