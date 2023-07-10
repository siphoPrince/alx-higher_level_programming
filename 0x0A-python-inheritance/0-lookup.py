#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
