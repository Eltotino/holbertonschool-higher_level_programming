#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry Class

    Attributes:
        width (int): width of the rectangle
        height (int):height of the rectangle
    """
    def __init__(self, width, height):
        """ Initialises the rectangle

        Args:
            width (int): width of the rectangle
            height (int):height of the rectangle.
            """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
