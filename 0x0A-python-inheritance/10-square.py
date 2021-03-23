#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class from Rectangle

    Attibutes:
        size (int): size of the square
    """
    def __init__(self, size):
        """Initialises the square

        Args:
            size(int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
