from fraction import *

def main():
    """ fraction class tests """
    frac1 = Fraction(3, 5)
    frac2 = Fraction(6, 3)
    frac3 = Fraction(3, 5)
    frac4 = Fraction(3, 4)
    frac5 = Fraction(1, 4)
    frac6 = Fraction(1, 2)
    addFrac = frac1 + frac2
    print(addFrac)
    print(frac1 == frac3)
    print(frac1 == frac2)
    print(frac5 <= frac4)

if __name__ == '__main__':
    main()
