#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Constructor for Rectangle class.
        Initializes the width and height of the rectangle.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: Height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        Returns:
            str: String representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ''
        return '\n'.join(['#' * self._width] * self._height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
            str: String representation of the rectangle object.
        """
        return 'Rectangle({}, {})'.format(self._width, self._height)
