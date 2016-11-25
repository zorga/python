#!/usr/bin/python

import sys
import math

def main():
    s = raw_input().strip() 
    s = s.replace(' ', '')
    l = len(s)
    rows = int(math.floor(math.sqrt(l)))
    columns = int(math.ceil(math.sqrt(l)))
    grid = [] 
    count = 0
    i = 0
    j = columns

    while count < rows:
        grid.append(s[i:j])
        i = i + columns
        j = j + columns
        count = count + 1

    k = 0
    res = ''

    for k in range(columns):
        for e in grid:
            if k < len(e):
                res += str(e[k])
        res += ' '

    print res
    
if __name__ == '__main__':
    main()
