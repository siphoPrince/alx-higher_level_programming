#!/usr/bin/python3
def uniq_add(my_list=[]):
    unList = set(my_list)
    n = 0

    for i in unList:
        n += i

    return (n)
