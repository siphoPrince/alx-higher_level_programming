#!/usr/bin/python3
'''
 A function that returns True if the object is an
 instance of a class that inherited from
'''


def is_kind_of_class(obj, a_class):
    """defines a () """
    return isinstance(obj, a_class) or isinstance(a_class, type(obj))
