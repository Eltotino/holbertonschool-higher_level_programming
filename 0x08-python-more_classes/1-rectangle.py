#!/usr/bin/python3
""" Rectangle module """


class Rectangle:

    """
    Class that defines a Rectangle

    Attributes:

    width: width of the rectangle
    height: height of the rectangle
    """

    def __init__(self, width, height):
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
    def width(self, width):
        """
        Setter of the width attribute

        Args:
            width(int):width of the rectangle

        Raises:
            TypeError: width must be an int
            ValueError: width must be <= 0
        """
        if not type(width) is int:
            raise TypeError("width must be an int")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        Getter of the height attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter of the height attribute

        Args:
            height(int): height of the rectangle

        Raises:
        TypeError: height must be an int
        ValueError: height must be <= 0
        """
        if not type(height) is int:
            raise TypeError("width must be an int")
        if height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = height
