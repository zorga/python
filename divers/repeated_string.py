#!/usr/bin/python

from collections import *
import sys

def main():
    s = raw_input().strip()
    l = long(raw_input().strip())
    n = 0

    for i in s:
        if i == 'a':
            n = n + 1

    res = n * (n / len(s))

    for i in s[:l % len(s)]:
        if i == 'a':
            res += 1

    print res

if __name__ == '__main__':
    main()
