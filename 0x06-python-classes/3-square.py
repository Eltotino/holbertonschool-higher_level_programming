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
        self.__size = size
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Public Method that returns the current square area"""
        return int(self.__size) * int(self.__size)
