#!/usr/bin/python

class Soldier:
    """The base class of all the soldiers of the game"""
    soldierCount = 0
    precision = 20 # a number evaluating the precision of the soldier

    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.pv = 50
        Soldier.soldierCount += 1

    def __repr__(self):
        return "Soldier()"

    def __str__(self):
        return "a specific soldier of the game"

    def printSoldierAttr(self):
        print('My name is ' + self.name + ' and I\'m from ' + self.country + ' !')

    def shoot(self, enemy):
        """enemy must be an instance of Soldier or one of its subclasses"""
        print('--> ' + self.name + ' is shooting ' + enemy.name + ' !!!')
        if(isinstance(enemy, Soldier)):
            enemy.pv -= 10
        else:
            print('enemy must be a valid soldier !')
        print(enemy.name + ' has lost 10 pv !')
        enemy.tellMyState()

    def tellMyState(self):
        """a method for the soldier to tells about his current state"""
        if(self.pv > 0):
            print(self.name + ' : Hahaha I\'m still alive ! I\'ve ' + str(self.pv) + 'PVs remaining !')
        else:
            print(self.name + ' : AAAaaaaarggghhH I\'m dead !')




class Sniper(Soldier):
    """A sniper shoot enemies from far away with a more precise weapon"""

    def __init__(self, name, country, weapon):
        self.name = name
        self.country = country
        self.weapon = weapon
        self.pv = 70
        Soldier.soldierCount += 1

    def printSniperAttr(self):
        Soldier.printSoldierAttr(self)
        print('I\'m a sniper ! So my weapon is a ' + self.weapon + ' !!! hahaha :D')

    def shoot(self, enemy):
        """Inherited from Soldier but Sniper shoot 30 pv instead of 10"""
        print('--> ' + self.name + ' is shooting ' + enemy.name + ' !!!')
        if(isinstance(enemy, Soldier)):
            enemy.pv -= 30
        else:
            print('enemy must be a valid soldier !')
        print('--> ' + enemy.name + ' has lost 30 pv !')
        enemy.tellMyState()


        