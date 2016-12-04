#!/usr/bin/python

import time

def main():
    n = int(raw_input().strip())
    assert 1 <= n <= 100
    print factorial(n)

def weak_factorial(n):
    '''
    inefficient implementation of factorial function
    '''
    if n == 0:
        return 1
    return n * weak_factorial(n - 1)

def factorial(n, acc=None):
    '''
    version of factorial function using an
    accumulator to be tail-recursive
    source : http://wiki.c2.com/?TailRecursion
    '''
    if acc is None:
        acc = 1

    if n == 0:
        return acc
    else:
        return factorial(n - 1, n * acc)

if __name__ == '__main__':
    main()
