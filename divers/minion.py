#!/usr/bin/python

import re

def main():
    voy = ['A', 'E', 'I', 'O', 'U']
    cons = []
    for i in range(1, 27):
        cons.append(chr(i + 64))
    cons = listdiff(cons, voy)

    s = raw_input().strip()
    s = s.upper()
    assert 0 <= len(s) <= 10**6

    score_stuart = score(calc_substr_list(s, cons))
    score_kevin = score(calc_substr_list(s, voy))

    if score_stuart == score_kevin:
        print("Draw")
    else:
        winner = max(score_stuart, score_kevin)
        if winner == score_stuart:
            print("Stuart " + str(score_stuart))
        else:
            print("Kevin " + str(score_kevin))

def listdiff(first, second):
    '''
    Computes the difference between lists 'first' and 'second'
    '''
    res = [i for i in first if i not in second]
    return res

def all_occurrences(substr, s):
    '''
    returns the indexes of all occurences of 'substr' in 's'
    '''
    # http://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
    res = [m.start() for m in re.finditer(substr, s)]
    return res

def calc_substr_list(s, alpha):
    '''
    find all substring starting with the letters in the alpha 'list' in 's'
    '''
    res = []
    begin_indexes = []

    sAlpha = [i for i in s if i in alpha]
    sAlpha = [c for c in set(sAlpha)]

    j = 0
    while (j < len(sAlpha)):
        curr_letter_positions = all_occurrences(sAlpha[j], s)
        for a in curr_letter_positions:
            for i in range(1, len(s[a:]) + 1):
                res.append(s[a:a + i])
        j = j + 1

    return res

def score(substr_list):
    '''
    computes the score given the 'substr_list'
    '''
    score_dict = {}
    for substr in substr_list:
        if substr not in score_dict:
            score_dict[substr] = 1
        else:
            score_dict[substr] = score_dict[substr] + 1
    
    score = 0
    for k in score_dict.keys():
        score = score + score_dict[k]
        
    return score

def kevin(s):
    '''
    find all substring starting with voyels in 's'
    '''
    return 0

if __name__ == '__main__':
    main()

