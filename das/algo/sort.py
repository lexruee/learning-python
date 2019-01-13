# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'


def selection_sort(array):
    n = len(array)

    def find_min(array, i, n):
        min_i = i
        for j in range(i, n):
            if array[j] < array[min_i]:
                min_i = j
        return min_i

    for i in range(n):
        # find the lowest element in the unsorted list
        min_i = find_min(array, i, n)
        if min_i != i:
            # swap the min element with the last element
            # from the sorted list
            a, b = array[i], array[min_i]
            array[i], array[min_i] = b, a


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key 


def quick_sort(array):
    def _quicksort(array, l, r):
        if l < r:
            p = _partition(array, l, r)
            _quicksort(array, l, p-1)
            _quicksort(array, p+1, r)

    def _partition(array, l, r):
        p = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] < p:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

    _quicksort(array, 0, len(array)-1)


def merge_sort(array):
    def _merge(l, r):
        m = []
        i, j = 0, 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                m.append(l[i])
                i += 1
            else:
                m.append(r[j])
                j += 1
        while i < len(l):
            m.append(l[i])
            i += 1
        while j < len(r):
            m.append(r[j])
            j += 1
        return m

    if len(array) <= 1:
        return array

    m = len(array)//2
    l = merge_sort(array[:m])
    r = merge_sort(array[m:])
    return _merge(l, r)


def counting_sort(array):
    pass