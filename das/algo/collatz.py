# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'


def collatz_fn(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def collatz_gen(x=0):
    def gen(n):
        while True:
            yield collatz_fn(n)
            n += 1

    return gen(x)
