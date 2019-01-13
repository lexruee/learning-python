#!/usr/bin/env python3

xs = range(0, 10)
ys = [x for x in xs if x >= 5]

zs = list(filter(lambda x: x >= 5, xs))

print("ys:", ys)
print("zs:", zs)
