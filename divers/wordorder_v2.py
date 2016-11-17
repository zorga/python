#!/usr/bin/python

from collections import *

def main():
    n = int(raw_input().strip())
    order = deque()
    cnt = Counter()

    for i in range(n):
        w = str(raw_input().strip())
        cnt[w] += 1
        if w not in order:
            order.appendleft(w)

    output = ""
    
    while order:
        e = order.pop()
        output += str(cnt[e]) + ' '
    print(len(cnt))
    print(output)

if __name__ == '__main__':
    main()
