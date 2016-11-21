#!/usr/bin/python

def main():
    n = int(raw_input().strip())
    # 'n' should not be greater than 26 and smaller than 0
    assert 0 < n < 27

    #for i in range(1, n + 1):
    i = n
    while i > 0:
        line = ""
        print chr(i + 96)
        i = i - 1

def build_line(i):
    pass
        

    

if __name__ == '__main__':
    main()
