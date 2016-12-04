#!/usr/bin/python2.7
'''
This a script to check if the randint function of the random module
generates some numbers multiple times
'''

import random
import operator
import collections

IRANGE = 1000

def main():
    '''Some fun'''
    lNumbers = []

    for i in range(0, IRANGE):
        tmp = random.randint(0, 1000)
        lNumbers += [tmp]

    cnt = collections.Counter(lNumbers)
    max_entry = max(cnt.iteritems(), key=operator.itemgetter(1))
    max_value = max_entry[0]
    max_occ = max_entry[1]

    print 'The number ' + str(max_value) + ' has been generated ' +  str(max_occ) + ' times'
    print 'It is generated ' + str(float(max_occ)/float(IRANGE)*100) + '% of the time'

if __name__ == '__main__':
    main()
