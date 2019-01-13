#!/usr/bin/env python3

xs = range(0, 10)
ys = [x + 1 for x in xs]

zs = list(map(lambda x: x + 1, xs))

print("ys:", ys)
print("zs:", zs)
