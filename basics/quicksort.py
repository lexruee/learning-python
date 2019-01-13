#!/usr/bin/env python3

import random

def quicksort(xs):
    if len(xs) <= 1:
        return xs
    else:
        pivot = xs[len(xs)//2]
        return quicksort(list(filter(lambda x: x < pivot, xs))) \
                + list(filter(lambda x: x == pivot, xs)) \
                + quicksort(list(filter(lambda x: x > pivot, xs)))


xs = [random.randint(0, 100) for _ in range(20)]
print("input:  ", xs)

ys = quicksort(xs)
print("output: ", ys)
