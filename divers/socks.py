import sys

def main():
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))

    shop = {}
    count = 0

    for sock in c:
        if sock not in shop:
            shop[sock] = 1
        else:
            if (shop[sock] % 2 != 0):
                count = count + 1
            shop[sock] = shop[sock] + 1
            
    print(count)

if __name__ == '__main__':
    main()
