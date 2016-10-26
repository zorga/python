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
shop_centers = []
roads = []
nmk = []


import sys


def main():
    '''
    The main function of the program
    '''
    parsing = parse_entry()

    if not parsing:
        print("Incorrect user's entries !")
        return

    # debug
    print(nmk)
    print(shop_centers)
    print(roads)

    # Run graph traversals by the cats
    big_cat = do_the_shopping(1, nmk[0])
    little_cat = do_the_shopping(1, nmk[0])


def check_list():
    '''
    check if the cats have purchased all types
    of fish
    '''
    currentList = big_cat + little_cat
    return len(set(currentList)) == nmk[2]


def do_the_shopping(start, dest):
    '''
    function that executes the graph traversal
    by the big and little cats
    The most important function !
    '''
    currPos = start
    groceries = []

    # First collect the fish from current position
     
    while (start != dest):
        # decrement currPos because shopping centers indices
        # begin at 1 and list indices begin at 0
        groceries.append(shop_centers[currPos - 1][1])

    return groceries 


def parse_entry():
    '''
    Parses the data entered by user and check the
    constraints
    '''
    res = 0

    # First line : N M K
    nmk.append(map(int, raw_input().strip().split(' ')))

    # next N lines : shop center description
    for i in range(nmk[0]):
        shop_centers.append(map(int, raw_input().strip().split(' ')))
    
    # next M lines : roads description
    for i in range(nmk[1]):
        roads.append(map(int, raw_input().strip().split(' ')))

    # Constraints
    assert 2 <= nmk[0] <= 10**3
    assert 1 <= nmk[1] <= (2 * (10**3)) 
    assert 1 <= nmk[2] <= 10
    
    for e in shop_centers:
        assert 0 <= e[0] <= nmk[2] 

        for aij in e[1:]:
            assert 1 <= aij <= nmk[2]

        # All aij are differents
        if len(e[1:]) > 1:
            assert len(e[1:]) != len(set(e[1:]))

    for e in roads:
        assert e[0] != e[1]
        assert 1 <= e[2] <= 10**4
    
    res = 1
    return res    
 

if __name__ == '__main__':
    main()
