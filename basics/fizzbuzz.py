#!/usr/bin/env python

import time


try:
    i = 0
    while True:
        i += 1
        time.sleep(1)

        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print('number {:d}'.format(i))

except KeyboardInterrupt:
    pass
