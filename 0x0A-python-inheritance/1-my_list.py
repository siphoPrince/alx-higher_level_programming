#!/usr/bin/python3
"""defines a class for mylist"""


class MyList(list):
    """represents the print sorted function"""
    def print_sorted(self):
        print(sorted(self))
