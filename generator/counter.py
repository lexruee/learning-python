#!/usr/bin/env python

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

if __name__ == '__main__':
    counter_it = counter(10)

    for _ in range(0, 6):
        print(next(counter_it))

    counter_it.send(6)

    for num in counter_it:
        print(num)
