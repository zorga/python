import sys

def square(n):
    i = 0
    a = 0 
    b = 1
    while i<n:
        i+=1
        a+=b
        b+=2
    return a

def main():
    result = square (sys.argv[1])
    print result 

if __name__ == '__main__':
    main()
