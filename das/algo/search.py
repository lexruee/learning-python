# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'


def binary_search(array, value, rec=True):
    if rec:
        return binary_search_rec(array, value, 0, len(array))
    else:
        return binary_search_iter(array, value)


def binary_search_iter(array, value):
    low, high = 0, len(array)
    
    while low <= high:
        mid = (low + high)//2
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_rec(array, value, low, high):
    if high < low:
        return -1

    mid = (low + high)//2
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binary_search_rec(array, value, mid+1, high)
    else:
        return binary_search_rec(array, value, low, mid-1)


def linear_search(array, value):
    r = -1
    for i, v in enumerate(array):
        if v == value:
            return i
    return r