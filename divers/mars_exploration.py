#!/usr/bin/python

import sys

def main():
    s = raw_input().strip()
    assert 1 <= len(s) <= 99
    assert len(s) % 3 == 0
    s = s.upper() 
    
    n_sos = len(s) / 3
    expected = "SOS" * n_sos
    legal = ['S', 'O']
    count = 0

    for i in range(len(s)):
        if s[i] != expected[i]:
            count = count + 1
    
    print count
    

if __name__ == '__main__':
    main()
