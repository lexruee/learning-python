#!/usr/bin/env python3

import random

def quicksort(xs):
    if len(xs) <= 1:
        return xs
    else:
        pivot = xs[len(xs)//2]
        return quicksort([x for x in xs if x < pivot]) \
                + [x for x in xs if x == pivot] \
                + quicksort([x for x in xs if x > pivot])


xs = random.sample(range(0, 100), 20)
print("input:  ", xs)

ys = quicksort(xs)
print("output: ", ys)
