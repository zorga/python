#!/bin/python

import sys

n = int(raw_input().strip())

for i in range(1, n + 1):
    diff = n - i
    tmp = "" + diff * ' ' + i * '#'
    print tmp
