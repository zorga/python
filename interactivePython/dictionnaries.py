#!/usr/bin/python3

import sys
import string
import math

def main():
    capitals = {'Iowa':'DesMoines', 'Wisconsin':'Madison'}
    print(capitals['Iowa'])
    capitals['Utah']='SaltLakeCity'
    print(capitals)
    capitals['California']='Sacramento'
    print(len(capitals))
    for i in capitals:
        print(capitals[i], " is the capital of ", i)

    aSet = set()
    print(type(aSet))

    for i in range(10):
        print(i**4)

    wordList = ['Nicolas', 'Paul', 'Xavier', 'Laurent', 'Marie', 'Leopold', 'Julien', 'Florent']
    for word in wordList:
        for l in word:
            aSet.add(l)
    print(aSet)

    alpha = []
    for i in range(42):
        alpha.append(i**2)
    # Alpha contains all the elements from 0 to 42 not included, exp 2

    anumber = int(input("Please enter a positive Integer : "))
    try:
        print(math.sqrt(anumber))
    except:
        print("You must enter a positive Integer !")
        print("Using the absolute value instead...")
        print(math.sqrt(abs(anumber)))


def lol():
    aName = input('Please enter your name : ')
    print('Your name in all capitals is ', aName.upper(), 'and has length', len(aName))

if __name__ == '__main__':
    main()
