# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'

def fermat_number(i):
    """
    Fi = 2^(2^i) + 1
    """
    return (1 << (1 << i)) + 1

def fermat_numbers(n):
    for i in range(0, n):
        yield fermat_number(i)
