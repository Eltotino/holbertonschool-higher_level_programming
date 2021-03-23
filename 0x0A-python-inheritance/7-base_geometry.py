#!/usr/bin/python3
"""Base Geometry module"""


class BaseGeometry:
    """Empty Class BaseGeomerty"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
