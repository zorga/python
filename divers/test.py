import sys

def isPrimeNumber (i):
    i = i%2
    
    if i == 0:
        r = True
    else:
        r = False

    return r

def addoneto (i, happy):
    if happy:
        i = i+1

    else:
        i = i+2

    return i

def main():
    s = "hi"
    print s[1]
    print len(s)
    age = 22
    print "Nicolas age is " + str(age)

if __name__ == '__main__':
    main()

