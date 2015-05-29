#!/usr/bin/python

from soldiers import *
import sys

def main():
    paul = Soldier('Paul', 'Belgium')
    leo = Sniper('Leopold', 'France', 'rifle')
    paul.shoot(leo)
    leo.shoot(paul)
    leo.shoot(paul)

if __name__ == '__main__':
    main()