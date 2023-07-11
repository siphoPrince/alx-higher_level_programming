#!/usr/bin/python3
"""defines a function"""


import json

def save_to_json_file(my_obj, filename):
    """refers to save to jason file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
