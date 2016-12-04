#!/usr/bin/python

from itertools import product

def main():
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    res = (list(product(A, B)))
    fin = ""
    for e in res:
        fin += str(e) + ' '
    print fin

if __name__ == '__main__':
    main()
