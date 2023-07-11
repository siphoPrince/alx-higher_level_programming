#!/usr/bin/python3
"""defines a write file ()"""


def write_file(filename="", text=""):
    """refers to a function write file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
