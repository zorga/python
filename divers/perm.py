#!/usr/bin/python

from itertools import permutations

def main():
    s, k = raw_input().strip().split(' ')
    k = int(k)
    perm = list(permutations(s, k))
    res = []

    for e in perm:
        tmp = ""
        for i in e:
            tmp += str(i)
        res.append(tmp)
    res.sort()
    
    for e in res:
        print e

if __name__ == '__main__':
    main()
