#!/usr/bin/python

def main():
    s = raw_input().strip()
    assert 0 <= len(s) <= 1000

    res = ""
    for c in s:
        if c.istitle():
            res += c.lower()
        else:
            res += c.upper()

    print res

if __name__ == '__main__':
    main()
