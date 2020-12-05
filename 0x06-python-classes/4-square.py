#!/usr/bin/python3
"""Square class with size"""


class Square():
    """Square defines the square of a given value

       Attributes:
            size: size of the square

    """
    def __init__(self, size=0):
        """
        Init method is a constructor for Square class

        Args:
            size (int): the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        A Getter of the instance attributes

        """
        return self.__size

    @size.setter
    def size(self, value):

        """
        Setter of instance attributes

        Args:
            value (int): a value for the square

        Raises:
            TypeError: size is not an int
            ValueError: size is less than 0
        """
        if not type(value) is int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Public Method that returns the current square area"""
        return (self.__size) * (self.__size)
