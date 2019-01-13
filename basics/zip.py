#!/usr/bin/env python3

a, b, c = range(0, 10), range(10, 21), range(20, 31)

zipped = zip(a, b, c)

for a, b, c in zipped:
    print(a, b, c)
