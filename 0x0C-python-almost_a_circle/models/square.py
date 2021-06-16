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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
    def update(self, *args, **kwargs):
        """ Updates the rectangles' attributes"""
        for num, obj in enumerate(args):
            if num == 0:
                self.id = obj
            if num == 1:
                self.size = obj
            if num == 2:
                self.x = obj
            if num == 3:
                self.y = obj     
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.width = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
