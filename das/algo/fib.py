# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'


def fib(n, rec=True):
    if rec:
        return fib_trec(n, 0, 1)
    else:
        return fib_iter(n)

def fib_trec(n, fn1=0, fn2=1):
    if n <= 0:
        return fn1
    else:
        return fib_trec(n-1, fn1 + fn2, fn1)

def fib_nrec(n):
    if n <= 0:
        return 0
    elif 0 < n <= 2:
        return 1
    else:
        return fib_nrec(n-1) + fib_nrec(n-2)

def fib_mrec(n, mem={1:1, 2: 1}):
    if n <= 0:
        return 0
    elif 0 < n <= 2:
        return 1
    else:
        n1, n2 = n - 1, n - 2
        if n1 not in mem:
            mem[n1] = fib_mrec(n-1, mem)
        if n2 not in mem:
            mem[n2] = fib_mrec(n-2, mem)
        
        mem[n] = mem[n1] + mem[n2]
        return mem[n]

def fib_iter(n):
    if n <= 0:
        return 0
    elif 0 < n <= 2:
        return 1
    else:
        fn1, fn2 = 1, 1
        for i in range(0, n-2):
            fn1, fn2 = fn1 + fn2, fn1
        return fn1

def fib_gen():
    def gen():
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b

    return gen()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: algo number")
        print("Options:")
        print("\talgo = trec | nrec | mrec | iter")
        print("")
    else:
        algo = sys.argv[1]
        num = int(sys.argv[2])
        fun = None
        if algo == 'trec':
            fun = fib_trec
        elif algo == 'mrec':
            fun = fib_mrec
        elif algo == 'nrec':
            fun = fib_nrec
        elif algo == 'iter':
            fun = fib_iter
        else:
            fun = fib_iter

        fn = fun(num)
        print("fib({})={}".format(num, fn))

