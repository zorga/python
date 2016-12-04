#!/usr/bin/python

def main():
    a = set()
    b = set()
    n, m = map(int, raw_input().strip().split(' '))
    arr = map(int, raw_input().strip().split(' '))
    map(a.add, raw_input().strip().split(' '))
    map(b.add, raw_input().strip().split(' '))
    
    happiness = 0

    for i in arr:
        if str(i) in a:
            happiness = happiness + 1
        if str(i) in b:
            happiness = happiness - 1

    print happiness

if __name__ == '__main__':
    main()
