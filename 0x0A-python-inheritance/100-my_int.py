#!/usr/bin/python3
'''
define a function for myint
'''


class MyInt(int):
    """represents a function"""

    def __eq__(self, value):
        return int(self) != int(value)

    def __ne__(self, value):
        return int(self) == int(value)
