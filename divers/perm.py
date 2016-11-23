#!/usr/bin/python

from itertools import permutations

def main():
    s, k = raw_input().strip().split(' ')
    k = int(k)
    perm = list(permutations(s, k))
    res = []

    for e in perm:
        tmp = ""
        tmp += str(e[0]) + str(e[1])
        res.append(tmp)
    res.sort()
    
    for e in res:
        print e

if __name__ == '__main__':
    main()
