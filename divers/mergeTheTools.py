#!/usr/bin/python

def main():
    s = raw_input().strip()
    k = int(raw_input().strip())
    assert 1 <= len(s) <= 10**4
    assert 1 <= k <= len(s) 
    assert len(s) % k == 0

    num_lines = len(s) / k
    sub_str = []
    limit = k
    i = 0

    while i < len(s):
        tmp = s[i:limit]
        sub_str.append(tmp)
        i = i + k
        limit = limit + k

    for word in sub_str:
        letters = set()
        sub = ""
        for c in word:
            if c not in letters:
                sub += c 
            letters.add(c)
        print sub

if __name__ == '__main__':
    main()
