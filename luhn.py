import sys

def main():
    try:
        i_cbn = int(raw_input('Please enter your account number : '))
    except ValueError:
        print 'You must enter a number !'
    s_cbn = str(i_cbn)
    i = len(s_cbn)-1
    while i >= 0:
        #print s_cbn[i]
        if i%2 != 0:
            print s_cbn[i]
        i = i-1
    exit(0)

if __name__ == '__main__':
    main()
