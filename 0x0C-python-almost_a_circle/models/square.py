#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class

    Attributes:
        size (int): square's size
        x (int): rectangle's horizontal axis
        y (int): rectangle's vertical axis
        id (int) : it's ID
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        self.size = size
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
            )
