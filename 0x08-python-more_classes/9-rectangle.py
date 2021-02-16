#!/usr/bin/python3

""" Rectangle module """


class Rectangle:

    """
    Class that defines a Rectangle

    Attributes:

        width: width of the rectangle
        height: height of the rectangle
        number_of_instances (int): public class attribute
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Init method is the constructor of the class Rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            value(int):positive int

        Raises:
            TypeError: value must be an int
            ValueError: value must be <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            value(int): positive int

        Raises:
        TypeError: if value not an int
        ValueError: value must be <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Prints the representation of the triangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = str(self.print_symbol)
        return ((rec*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """
        Representation of the class

        Returns the string representation(str)
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Delete the instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare 2 rectangles

        Args:
        Rect_1: rectangle
        Rect_2: rectangle

        Raises:
        TypeError: if Rect_1 or Rect_2 is not an instance of Rectangle

        Return:
        The biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        aire_1 = rect_1.area()
        aire_2 = rect_2.area()
        if aire_1 >= aire_2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        A rectangle is a square
        """
        return (cls(size, size))
