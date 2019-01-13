#!/usr/bin/env python3

from functools import reduce

xs = range(1, 11)
acc = reduce(lambda acc, n: acc + n, xs)

print("xs: ",  list(xs))
print("acc: ", acc)
