#!/usr/bin/env python

even = (str(x) for x in range(100) if x % 2 == 0)
odd = (str(x) for x in range(100) if x % 2 != 0)

print("even: ", end=' ')
print(",".join(even))

print("odd:  ", end=' ')
print(",".join(odd))

