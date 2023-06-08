#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import div
from calculator_1 import mul

a = 10
b = 5

sumof = add(a, b)
print("{} + {} = {}".format(a,b,sumof))

divof = div(a, b)
print("{} / {} = {}".format(a,b,divof))

subof = sub(a, b)
print("{} - {} = {}".format(a,b,subof))

multof = mul(a, b)
print("{} * {} = {}".format(a,b, multof))
