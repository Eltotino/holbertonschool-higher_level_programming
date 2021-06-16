#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Attributes:
        width (int): rectangle's width
        height (int): rectangle's height
        x (int): rectangle's horizontal axis
        y (int): rectangle's vertical axis
        id (int) : it's ID
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """ displays the rectangle shape with'#'"""
        print("{}".format("\n"*self.y), end='')
        for i in range(self.height):
            print("{}{}".format(" "*self.x, "#"*self.width))

    def __str__(self):
        """Return a string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
            )

    def update(self, *args, **kwargs):
        """ Updates the rectangles' attributes"""
        for num, obj in enumerate(args):
            if num == 0:
                self.id = obj
            if num == 1:
                self.width = obj
            if num == 2:
                self.height = obj
            if num == 3:
                self.x = obj
            if num == 4:
                self.y = obj
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
