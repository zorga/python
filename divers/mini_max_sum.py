#!/bin/python

import sys

def main():
    l = map(int, raw_input().strip().split(' '))
    l2 = list(l)

    min_sum = 0
    max_sum = 0
    i = 0

    while i < 4:
        min_index = l.index(min(l))
        min_sum = min_sum + l[min_index]
        del l[min_index]

        max_index = l2.index(max(l2))
        max_sum = max_sum + l2[max_index]
        del l2[max_index]

        i = i + 1

    print min_sum, max_sum
        
if __name__ == '__main__':
    main()


