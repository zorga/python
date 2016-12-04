#!/usr/bin/python

def main():
    n = int(raw_input().strip())
    # 'n' should not be greater than 26 and smaller than 0
    assert 0 < n < 27
    
    alphabet = []
    for i in range(1, n + 1):
        alphabet.append(chr(i + 96))

    rang = ""

    for i in range(len(alphabet)):
        if i <= 0:
            rang += build_line(alphabet[i:])
        else:
            tmp = "" + 2*i*'-' + build_line(alphabet[i:]) + 2*i*'-'
            rang = tmp + '\n' + rang + '\n' + tmp

    print rang

def build_line(letters):
    '''
    build a single line of the rangoli game
    '''
    res = "" + letters[0]
    i = 1
    
    while i < len(letters):
        res = '-' + res + '-'
        res = letters[i] + res + letters[i]
        i = i + 1

    return res
        
        

    

if __name__ == '__main__':
    main()
