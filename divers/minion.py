#!/usr/bin/python


def main():
    voy = ['A', 'E', 'I', 'O', 'U']
    cons = []
    for i in range(1, 27):
        cons.append(chr(i + 64))
    cons = listdiff(cons, voy)
    print(cons)

    s = raw_input().strip()
    s = s.upper()
    #stuart = stuart(s)
    #kevin = kevin(s)

def listdiff(first, second):
    '''
    Computes the difference between lists 'first' and 'second'
    '''
    res = [i for i in first if i not in second]
    return res

def stuart(s):
    '''
    find all substring starting with consonents in 's'
    '''
    return 0

def kevin(s):
    '''
    find all substring starting with voyels in 's'
    '''
    return 0

if __name__ == '__main__':
    main()

