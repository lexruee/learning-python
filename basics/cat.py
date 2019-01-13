#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    content = []
    for fi in sys.argv[1:]:
        with open(fi) as f:
            for line in f.readlines():
                print(line.strip())
