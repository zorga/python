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

def parseEntry():
    '''
    Parses the data entered by user and check the
    constraints
    '''
    # First line : N M K
    nmk = map(int, raw_input().strip().split(' '))
    # next N lines : shop center description
    shopCenters = []
    # next M lines : roads description
    roads = []

    for i in range(nmk[0]):
        shopCenters.append(map(int, raw_input().strip().split(' ')))
    
    for i in range(nmk[1]):
        roads.append(map(int, raw_input().strip().split(' ')))

    # Constraints
    assert 2 <= nmk[0] <= 10**3
    assert 1 <= nmk[1] <= (2 * (10**3)) 
    assert 1 <= nmk[2] <= 10
    
    for e in shopCenters:
        assert 0 <= e[0] <= nmk[2] 

        for aij in e[1:]:
            assert 1 <= aij <= nmk[2]

        # All aij are differents
        if len(e[1:]) > 1:
            assert len(e[1:]) != len(set(e[1:]))

    for e in roads:
        assert e[0] != e[1]
        assert 1 <= e[2] <= 10**4
    
    return nmk, shopCenters, roads
 

if __name__ == '__main__':
    main()
