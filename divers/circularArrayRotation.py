#!/bin/python

import sys

def main():
    n, k, q = raw_input().strip().split(' ')
    n, k, q = [int(n),int(k),int(q)]
    a = map(int,raw_input().strip().split(' '))
    
    if k > n:
        k = k % n

    res = ""
    for a0 in xrange(q):
        m = int(raw_input().strip())

        # Compute the right indice :
        i = m + n - k
        # If the new indice is bigger than n :
        if i >= n:
            i = i % n
        res += str(a[i]) + '\n'

    print res[:-1]
        
if __name__ == '__main__':
    main()
