#!/usr/bin/python3
"""Defines a JSON writing function."""
import json


def save_to_json_file(my_obj, filename):
    """defines a JSON representation."""
    with open(filename, "w") as l:
        json.dump(my_obj, l)
