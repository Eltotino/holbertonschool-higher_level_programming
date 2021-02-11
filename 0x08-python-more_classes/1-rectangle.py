#!/usr/bin/python3
""" Rectangle module """


class Rectangle:

    """
    Class that defines a Rectangle

    Attributes:

    width: width of the rectangle
    height: height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Init method is the constructor of the class Rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Getter of the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of the width attribute

        Args:
            value(int):width of the rectangle

        Raises:
            TypeError: width must be an int
            ValueError: width must be <= 0
        """
        if not type(value) is int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter of the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of the height attribute

        Args:
            value(int): height of the rectangle

        Raises:
        TypeError: height must be an int
        ValueError: height must be <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
