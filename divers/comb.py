#!/usr/bin/python

from itertools import combinations

def main():
    s, k = raw_input().strip().split(' ')
    k = int(k)
    res = []

    for i in range(1, k + 1):
        tmp = list(combinations(s, i))
        tmp.sort()
        res += tmp

    for e in res:
        print e
    

if __name__ == '__main__':
    main()
