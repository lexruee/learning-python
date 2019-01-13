# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'

def gcd(a, b, rec=False):
    if rec:
        return gcd_rec(a, b)
    else:
        return gcd_iter(a, b)

def gcd_iter(a, b):
    if b == 0:
        return a
    else:
        while b != 0: 
            r = a % b
            a, b = b, r
        return a

def gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)
