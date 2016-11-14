#!/bin/bash

import sys

def main():
    t1, t2, n = map(int, raw_input().strip().split(' '))
    assert 0 <= t1 <= 2
    assert 0 <= t2 <= 2
    assert 3 <= n <= 20

    for i in range(2, n):
        fibo = t1 + (t2**2)
        t1 = t2
        t2 = fibo
    print(fibo)

if __name__ == '__main__':
    main()
