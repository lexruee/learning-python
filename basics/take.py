#!/usr/bin/env python3

import itertools

def fib():
    a, b = 0, 1
    while True:
        b, a = a + b, b
        yield a

count = itertools.count()

fibs = [f for f in itertools.takewhile(lambda _: next(count) < 10, fib())]
print(fibs)

