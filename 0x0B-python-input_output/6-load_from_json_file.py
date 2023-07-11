#!/usr/bin/python3
"""Defines a JSON reading file function."""
import json


def load_from_json_file(filename):
    """defiens a load file."""
    with open(filename) as l:
        return json.load(l)
