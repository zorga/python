#!/usr/bin/python

def main():
    s = raw_input().strip()
    prev = True
    res = ""
    assert 0 <= len(s) <= 1000

    for char in s:
        if prev:
            char = char.upper()

            if char != ' ':
                prev = False

        if char == ' ':
            prev = True
        
        res += char
    
    print(res)

if __name__ == '__main__':
    main()

