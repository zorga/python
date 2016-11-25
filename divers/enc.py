#!/usr/bin/python

import sys
from math import ceil, sqrt

def main():
    s = raw_input().strip()
    s = s.replace(' ', '')
    c = int(ceil(sqrt(len(s))))
    print(' '.join(map(lambda x: s[x::c], range(c)))) 

if __name__ == '__main__':
    main()
