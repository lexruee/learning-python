# -*- coding:utf-8 -*-


def rec_eq(x, y):
    if x <= 0 or y <= 0:
        return 0
    else:
        return x + y + rec_eq(x - 1, y)


def rec_acc(x, y, acc = 0):
    if x <= 0 or y <= 0:
        return acc
    else:
        return rec_acc(x - 1, y, acc + x + y)


def rec_iter(x, y):
    acc = 0
    if x <= 0 or y <= 0:
        return acc

    while x > 0:
        acc += x + y
        x -= 1

    return acc


def rec_solved(x, y):
    acc = 0
    if x <= 0 or y <= 0:
        return acc
    acc = x * y + int(x * (x+1)/2)
    return acc

