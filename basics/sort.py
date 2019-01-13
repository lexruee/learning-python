#!/usr/bin/env python3

import random

xs = random.sample(range(0, 100), 20)
ys = xs[:] # copy list
ys.sort()
zs = sorted(xs)
qs = sorted(xs, reverse=True)

print("xs:  ", xs)
print("ys:  ", ys)
print("zs:  ", zs)
print("qs:  ", qs)
