#!/bin/python

import sys

def main():
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))
    count = 0
    
    assert 2 <= n <= 100
    assert 1 <= k <= 100
    for ai in a:
        assert 1 <= ai <= 100

    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if (i < j):
                if ((a[i] + a[j]) % k == 0):
                    count = count + 1
    print(count)


if __name__ == '__main__':
    main()
