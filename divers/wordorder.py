#!/usr/bin/python

def main():
    n = int(raw_input().strip())
    words = {}
    order = {}
    for i in range(n):
        w = str(raw_input().strip())
        if w not in order:
            order[w] = i
        if w not in words:
            words[w] = 1
        elif w in words:
            words[w] = words[w] + 1

    output = ""
    count = 0
    for i in range(n):
        if order:
            count = count + 1
            curr = min(order, key=order.get)
            del order[curr]
            output += str(words[curr]) + ' '
    print(count)
    print(output.strip())


if __name__ == '__main__':
    main()
