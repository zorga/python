import sys

from fraction import *

def performTests():
    """method for testing the fraction operators"""
    frac1 = Fraction(3, 5)
    frac2 = Fraction(6, 3)
    frac3 = Fraction(3, 5)
    frac4 = Fraction(3, 4)
    frac5 = Fraction(1, 4)
    frac6 = Fraction(1, 2)
    frac7 = Fraction(-1, 3)
    frac8 = Fraction(-2, 3)
    resultAdd = Fraction(13, 5)
    score = 0

    corrEq = (True == (frac1 == frac3))
    if corrEq:
        print("Equality operator : pass")
        score += 1
    else:
        print("Equality operator : failed")

    corrLe = (True == (frac8 <= frac7))
    if corrLe:
        print("Less than or equal to operator : pass")
        score += 1
    else:
        print("Less than or equal to operator : failed")

    corrNe = (True == (frac5 != frac6))
    if corrNe:
        print("Not equal to operator : pass")
        score += 1
    else:
        print("Not equal to to operator : failed")

    corrAdd = ((frac1 + frac2) == resultAdd)
    if corrAdd:
        print("Addition operator : pass")
        score += 1
    else:
        print("Addition operator : failed")

    corrSub = ((frac4 - frac6) == frac5)
    if corrSub:
        print("Substraction operator : pass")
        score += 1
    else:
        print("Substraction operator : failed")
    print("--> Score : " + str(score) + "/5")

def checkInput(user):
    """
    Check if the String user if in the form \"n/d\"
    returns False otherwise
    """
    res = False
    if len(user) == 3 and user[1] == "/":
        if user[0].isdigit() and user[2].isdigit():
            res = True
    return res

def parseInput():
    """
    parse the fraction provided by the user in a String of the form
    1/4, or 1/9, or 7/3, etc. and returns a Fraction object
    """
    res = None
    fracString = input('Enter your fraction in the form "n/d" : ')
    if checkInput(fracString):
        Num = int(fracString[0])
        Den = int(fracString[2])
    else:
        print("Invalid input ! Aborting...")
        sys.exit()
        # frac[1] is the "/" character of the function
    try:
        res = Fraction(Num, Den)
    except:
        print("!!! The denominator must be greater than zero !!!")
        print("--> The denominator will be set to 1 by default...")
        res = Fraction(Num, 1)
    return res

def main():
    """ fraction class tests """
    # INITIALIZING THE FUNCTIONS :
    userFrac = parseInput()
    print(userFrac)

    # TESTING PART :
    # performTests()


if __name__ == '__main__':
    main()
