#!/usr/bin/python

def main():
    n = float(raw_input().strip())
    l = map(float, raw_input().strip().split(' '))
    assert int(n) == len(l)
    pos = 0
    neg = 0
    nul = 0
    percentage = 1.0 / n

    for e in l:
        if e < 0:
            neg += percentage
        elif e > 0:
            pos += percentage
        elif e == 0:
            nul += percentage

    print pos
    print neg
    print nul

if __name__ == '__main__':
    main()
