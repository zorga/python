#!/usr/bin/python

from collections import *
import time

def main():
    n = int(raw_input().strip())
    words = [raw_input().strip() for i in range(n)]
    cnt = Counter(words)
    
    print len(cnt)

    for word in words:
        derp = cnt.pop(word, None)
        if derp == None:
            continue
        else:
            print derp,

if __name__ == '__main__':
    main()
