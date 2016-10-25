import sys

def main():
    s = raw_input().strip()
    assert 1 <= len(s) <= 10**5

    words = 1
    for letter in s:
        if letter.istitle():
            words = words + 1

    print(words)

if __name__ == '__main__':
    main()
