# -*- coding:utf-8 -*-


def factorial_rec(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial_acc(n, acc=1):
    if n <= 1:
        return acc
    else:
        return factorial_acc(n - 1, acc * n)


def factorial_gen():
    def gen():
        r, i = 1, 1
        while True:
            yield r
            i += 1
            r *= i

    return gen()
