#!/usr/bin/python

def main():
    heights = map(int, raw_input().strip().split(' '))
    assert len(heights) == 26
    word = str(raw_input().strip())
    curr_height = 0
    
    for c in word:
        indice = ord(c) - 97
        height = heights[indice] 
        if height > curr_height:
            curr_height = height

    print curr_height * len(word)

if __name__ == '__main__':
    main()
