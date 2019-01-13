#!/usr/bin/env python

def fib(n):
    fn = fn1 = fn2 = 1
    yield fn2
    yield fn1
    for i in range(0, n):
        fn = fn1 + fn2
        fn1, fn2 = fn, fn1
        yield fn

for i in fib(10):
    print(i)
