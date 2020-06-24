#!/usr/bin/python3
"""Square class with size"""


class Square():
    """Square defines the square of a given value

       Attributes:
            size: size of the square

    """
    def __init__(self, size):
        """
        Init method is a constructor for Square class

        Args:
            size (int): the size of the square
        """
        self.__size = size
