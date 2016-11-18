#!/usr/bin/python

import sys

def main():
    a0, a1, a2 = map(int, raw_input().strip().split(' '))
    b0, b1, b2 = map(int, raw_input().strip().split(' '))
    
    alice = 0
    bob = 0
    
    if a0 != b0:
        if a0 > b0:
            alice = alice + 1
        else:
            bob = bob + 1

    if a1 != b1:
        if a1 > b1:
            alice = alice + 1
        else:
            bob = bob + 1

    if a2 != b2:
        if a2 > b2:
            alice = alice + 1
        else:
            bob = bob + 1

    print alice, bob

if __name__ == '__main__':
    main()
