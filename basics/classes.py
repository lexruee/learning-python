#!/usr/bin/env python3

class A:
    pass

class B(A):
    pass

class C(B):
    pass


a = A()
b = B()
c = C()

assert type(a) == A
assert isinstance(a, A)

assert type(b) == B
assert isinstance(b, B)
assert isinstance(b, A)

assert type(c) == C
assert isinstance(c, C)
assert isinstance(c, B)
assert isinstance(c, A)

assert issubclass(B, A)
assert issubclass(C, B)
assert issubclass(C, A)
