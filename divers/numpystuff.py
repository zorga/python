#!/usr/bin/python

import numpy

def main():
    n, m = map(int, raw_input().strip().split(' '))
    cols = []

    for i in range(n):
        tmp = map(int, raw_input().strip().split(' '))
        cols.append(tmp)

    arr = numpy.array(cols)
    print numpy.transpose(arr)
    print arr.flatten()
    

        

if __name__ == '__main__':
    main()
