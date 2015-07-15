#!/usr/bin/python3

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        """overrides the __str__ method to print the Fraction objects nicely"""
        return str(self.num) + "/" + str(self.den)

    def sameDenominatorNum(frac1, frac2):
        @staticmethod
        firstNum = (frac1.num * frac2.den)
        secondNum = (frac1.den * frac2.num)
        return [firstNum, secondNum]

    def __add__(self, otherFraction):
        """this method overrides the + operator definition for allowing us to
        use it with Fraction objects"""
        newNum = (self.num * otherFraction.den) + (self.den * otherFraction.num)
        newDen = self.den * otherFraction.den
        #Factoring the result :
        common = self.gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __le__(self, other):
        """Overrides the equality less than or equal to operator"""
        fracs = sameDenominatorNum(self, other)
        return fracs[1] <= fracs[2]

    def __eq__(self, other):
        """Overrides the equality operator to be able to compare to fraction
        object. Compares the values, not the references"""
        fracs = sameDenominatorNum(self, other)
        return fracs[1] == fracs[2]

    def gcd(self, m, n):
        """Calculate the Greatest common divisor of m and n and returns it"""
        while (m % n) != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n
