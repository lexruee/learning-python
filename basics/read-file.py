#!/usr/bin/env python3

with open('test.txt') as f:
    data = f.readlines()

for row in data:
    print(row.strip())
