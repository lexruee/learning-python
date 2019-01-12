#!/usr/bin/env python

from functools import reduce

"""
https://de.wikipedia.org/wiki/Lateinisches_Quadrat
"""

MAT_STR = """\
        4 3 1 2
        3 4 2 1
        2 1 3 4
        1 2 4 3"""

def parse_mat_str(mat_str):
    return [ list(map(int, row.strip().split())) for row in mat_str.split("\n") ]

assert parse_mat_str(MAT_STR) == [[4, 3, 1, 2], [3, 4, 2, 1], [2, 1, 3, 4], [1, 2, 4, 3]]

def check_row_sum(row):
    n = len(mat)
    return sum(row) == n * (n + 1)//2

def check_mat(mat):
    return reduce(lambda a, b: a and b, [check_row_sum(row) for row in mat])

if __name__ == '__main__':
    mat = parse_mat_str(MAT_STR)
    print(check_mat(mat))

