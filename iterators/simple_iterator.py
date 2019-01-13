#!/usr/bin/env python

def take(n):
    for i in range(0, n):
        yield i

for i in take(10):
    print(i)
