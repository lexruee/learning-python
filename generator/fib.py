#!/usr/bin/env python

def fib():
    a, b = 0, 1
    while True:
        b, a = a + b, b
        yield a

if __name__ == '__main__':
    fib_iter = fib()
    fibs = list(map(lambda _: next(fib_iter), range(10)))
    print(fibs)

