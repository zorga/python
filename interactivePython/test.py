from fraction import *

def main():
    """ fraction class tests """
    frac1 = Fraction(3, 5)
    frac2 = Fraction(6, 3)
    frac3 = Fraction(3, 5)
    frac4 = Fraction(3, 4)
    frac5 = Fraction(1, 4)
    frac6 = Fraction(1, 2)
    resultAdd = Fraction(13, 5)

    # TESTING PART :

    corrEq = (True == (frac1 == frac3))
    if corrEq:
        print("Equality operator : pass")
    else:
        print("Equality operator : failed")

    corrLe = (True == (frac5 <= frac4))
    if corrLe:
        print("Less than or equal to operator : pass")
    else:
        print("Less than or equal to operator : failed")

    corrNe = (True == (frac5 != frac6))
    if corrNe:
        print("Not equal to operator : pass")
    else:
        print("Not equal to to operator : failed")

    corrAdd = ((frac1 + frac2) == resultAdd)
    if corrAdd:
        print("Addition operator : pass")
    else:
        print("Addition operator : failed")

    corrSub = ((frac4 - frac6) == frac5)
    if corrSub:
        print("Substraction operator : pass")
    else:
        print("Substraction operator : failed")

if __name__ == '__main__':
    main()
