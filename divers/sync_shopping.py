'''
This is my solution to the hackerrank challenge :
Synchronous Shopping in the Graph Theory section
'''

__author__ = "Nicolas Ooghe"

# Define globals here

# the cats are represented using lists showing the
# types of fish they've already purchased
# The concatenation of both lists must correspond to
# all the fish types (collective purchasing)
big_cat = []
little_cat = []

import sys

def main():
    '''
    The main function of the program
    '''
    nmk, shopCenters, roads = parseEntry()
    print(nmk)
    print(shopCenters)
    print(roads)

def parseEntry():
    '''
    Parses the data entered by user and check the
    constraints
    '''
    # First line : N M K
    nmk = map(int, raw_input().strip().split(' '))
    # next N lines : shop center description
    shopCenters = [][]
    # next M lines : roads description
    roads = [][]

    for i in range(nmk[0]):
        shopCenters[i] = map(int(raw_input().split().strip(' ')))
    
    for i in range(nmk[1]):
        roads[i] = map(int(raw_input().split().strip(' ')))
    
    return nmk, shopCenters, roads
 

if __name__ == '__main__':
    main()
