#!/usr/bin/python3
"""defines a baseGeometry function"""


class BaseGeometry:
    """refers to a basegeometry"""
    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
