#!/bin/python

import sys

def main():
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    
    assert 1 <= n <= 1000
    for ai in arr:
        assert 1 <= ai <= 1000
        
    while (1): 
        print(len(arr))
        cut = min(arr)
        count = 0
        res = []
        for i in range(0, len(arr)):
            arr[i] = arr[i] - cut
            if arr[i]:
                res.append(arr[i])
        if not len(res):
            break

        arr = res
    
if __name__ == '__main__':
    main()
