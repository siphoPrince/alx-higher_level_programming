#!/usr/bin/python3
'''
 Import module
 '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    defines a square class
    '''

    def __init__(self, size):
        """ init setup """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        '''
        Set a sting
        '''
        return ("[Square] {}/{}".format(self.__size, self.__size))
