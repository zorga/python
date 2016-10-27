'''
This is my solution to the hackerrank challenge :
Synchronous Shopping in the Graph Theory section
'''

__author__ = "Nicolas Ooghe"

# Define globals here

'''
the cats are represented using lists showing the
types of fish they've already purchased
The concatenation of both lists must correspond to
all the fish types (collective purchasing)
(at the end of the shopping of course)
'''
debug = 1
big_cat = []
little_cat = []

#NMK, shops, edges = 0, 0, 0
# Hard-coded sample input during debuggin :
NMK = [5, 5, 5]
shops = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
edges = [[1, 2, 10], [1, 3, 10], [2, 4, 10], [3, 5, 10], [4, 5, 10]]


import sys


def main():
    '''
    The main function of the program
    '''
    # Uncomment the following lines to test other inputs
    #nmk, shop_centers, roads = parse_entry()
    # Binding the globals to the user's data :
    #NMK, shops, edges = nmk, shop_centers, roads

    if debug:
        print(NMK)
        print(shops)
        print(edges)

    adjmatrix()


def adjmatrix():
    '''
    Build an adjacency matrix representing the graph
    '''
    res = []
    i = 0
    for v in range(NMK[0]):
        res.append([0 for item in range(NMK[0])])
    print(res)


def check_list():
    '''
    check if the cats have purchased all types
    of fish
    '''
    currentList = big_cat + little_cat
    return len(set(currentList)) == NMK[2]


def do_the_shopping():
    '''
    function that executes the graph traversal
    by the big and little cats
    The most important function !
    '''
    currPos = start
    groceries = []

    return groceries 


def parse_entry():
    '''
    Parses the data entered by user and check the
    constraints
    '''
    res = 0

    shop_centers = []
    roads = []

    # First line : N M K
    nmk = map(int, raw_input().strip().split(' '))

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
    return nmk, shop_centers, roads
 

if __name__ == '__main__':
    main()
