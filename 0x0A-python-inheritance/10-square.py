#!/usr/bin/python3
""" Import module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represents a square class """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
