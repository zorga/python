#!/usr/bin/python

from collections import *
import sys

def main():
    s = raw_input().strip()
    n = long(raw_input().strip())

    ss = s * n
    cnt = Counter(ss)
    print cnt['a']
    

if __name__ == '__main__':
    main()