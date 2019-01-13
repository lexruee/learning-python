#!/usr/bin/env python

import time

def fizzbuz(n=None):
    i = 0
    
    while n is None or i < n:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            yield i
        elif i % 3 == 0:
            print('Fizz')
            yield i
        elif i % 5 == 0:
            print('Buzz')
            yield i
        else:
            yield False

try:
    for x in fizzbuz():
        if x:
            print(x)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
