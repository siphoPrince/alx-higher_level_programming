#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndir = a_dictionary.copy()
    list_keys = list(ndir.keys())

    for i in list_keys:
        ndir[i] *= 2

    return (ndir)
