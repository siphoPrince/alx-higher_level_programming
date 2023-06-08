#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

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
