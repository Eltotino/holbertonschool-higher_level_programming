#!/usr/bin/python3
"""Square class with size"""


class Square():
    """Square defines the square of a given value

       Attributes:
            size: size of the square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Init method is a constructor for Square class

        Args:
            size (int): the size of the square
            position(tuple): a tuple of integer to show the
            position of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        A Getter of the instance attributes

        """
        return self._size

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

    @property
    def position(self):
        """
        Getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position attribute

        Args:
            Value(tuple) : represents the position of the square

        Raises:
            TypeError: position is not tuple and has 2 integers

        """
        if not type(value) is tuple or len(value) != 2\
                or value[0] < 0 or value[1] < 0 or not type(value[0]) is int \
                or not type(value[1]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Public Method that returns the current square area"""
        return (self.__size) * (self.__size)

    def my_print(self):
        """
        Prints thevalue of square formed by "#""

        """
        if self.__size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end="")
                print('#' * self.__size)
