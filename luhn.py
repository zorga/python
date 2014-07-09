import sys

def main():
    try:
        i_cbn = int(raw_input('Please enter your account number : '))
    except ValueError:
        print 'You must enter a number !'
    result = luhn(i_cbn)
    print result

def luhn(i_cbn):
    s_cbn = str(i_cbn)
    i = len(s_cbn)-2
    lsum = int(s_cbn[i+1])
    while i >= 0:
        #print s_cbn[i]
        op = int(s_cbn[i])*2
        if op > 9:
            tosum = str(op)
            a = int(tosum[0]) + int(tosum[1])
            lsum += a
        else:
            lsum += op
        if i-1 >= 0:
            lsum += int(s_cbn[i-1])
        i = i-2
    return lsum

if __name__ == '__main__':
    main()
