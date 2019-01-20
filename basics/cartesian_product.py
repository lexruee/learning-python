#!/usr/bin/env python3

import itertools


tuples = itertools.permutations(range(3),2)
print(list(tuples))

triples = itertools.permutations(range(4),3)
print(list(triples))
