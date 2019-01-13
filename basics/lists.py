#!/usr/bin/env python3

x = range(0, 10)
x2 = [x**2 for x in range(0, 10)]

for y, z in zip(x, x2):
    print("f({0}) = {0}^2 = {0}*{0} = {1}".format(y, z))
