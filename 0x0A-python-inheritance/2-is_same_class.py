#!/usr/bin/python3
'''returns True if the object is instance'''


def is_same_class(obj, a_class):
    """represents a function"""
    return issubclass(a_class, type(obj))
