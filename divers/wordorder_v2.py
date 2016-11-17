#!/usr/bin/python

from collections import *
import time

def main():
    n = int(raw_input().strip())
    words = [raw_input().strip() for i in range(n)]
    # remove duplicates and count them using Counter collection
    cnt = Counter(words)
    
    print len(cnt)

    for word in words:
        # here we add 'None' arg in case 'word' isn't in the counter anymore
        derp = cnt.pop(word, None)
        if derp == None:
            continue
        else:
            print derp,

if __name__ == '__main__':
    main()
