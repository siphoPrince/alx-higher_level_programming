#!/usr/bin/python3
"""defines a readfile function"""


def read_file(filename=""):
    """refers to a read file function"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
