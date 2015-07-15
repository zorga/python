#!/usr/bin/python3

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        # We check if the bottom part of the fraction is greater than zero
        if bottom <= 0:
            raise ValueError("The denominator must be greater than zero !!!")
        else:
            self.den = bottom

    def __str__(self):
        """overrides the __str__ method to print the Fraction objects nicely"""
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherFraction):
        """this method overrides the + operator definition for allowing us to
        use it with Fraction objects"""
        newNum = (self.num * otherFraction.den) + (self.den * otherFraction.num)
        newDen = self.den * otherFraction.den
        #Factoring the result :
        common = self.gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __sub__(self, otherFraction):
        """this method overrides the - operator definition for allowing us to
        use it with Fraction objects"""
        newNum = (self.num * otherFraction.den) - (self.den * otherFraction.num)
        newDen = self.den * otherFraction.den
        #Factoring the result :
        common = self.gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __le__(self, other):
        """Overrides the less than or equal to operator"""
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum <= secondNum

    def __lt__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum < secondNum

    def __ne__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum != secondNum

    def __gt__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum > secondNum

    def __ge__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum >= secondNum

    def __eq__(self, other):
        """Overrides the equality operator to be able to compare to fraction
        object. Compares the values, not the references"""
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum == secondNum

    def gcd(self, m, n):
        """Calculate the Greatest common divisor of m and n and returns it"""
        while (m % n) != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n
