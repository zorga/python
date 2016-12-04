#!/usr/bin/python

import sys
import math

def main():
    # users input
    s = raw_input().strip() 
    s = s.replace(' ', '')
    l = len(s)
    rows = int(math.floor(math.sqrt(l)))
    columns = int(math.ceil(math.sqrt(l)))
    
    # check constraints
    assert rows < columns
    assert rows * columns >= l

    grid = [] 

    for i in range(0, l, columns):
        grid.append(s[i:i + columns])
    
    print grid

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
