import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be int")
        if isinstance(denominator, bool):
            raise TypeError("Denominator must be int")
        gcd = math.gcd(numerator,denominator)
        if gcd == 0:
            # avoid division by 0
            gcd = 1
        if denominator < 0:
            gcd = -gcd
        # this both removes gcd and ensures denominator >= 0
        self.numerator = numerator//gcd
        self.denominator = denominator//gcd


    def __str__(self):
        """Return the string in form "a/b" when a is numerator and b is denominator.
        (or "a" when a equals to 0 or "b" equals to 1)
        """
        if self.denominator == 1:
           # show value as integer
           return str(self.numerator)
        return '{0}/{1}'.format(self.numerator, self.denominator)
    
    def __neg__(self):
        """Return negation of a fraction"""
        return Fraction(-self.numerator, self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        num = self.numerator * frac.denominator + frac.numerator * self.denominator
        denom = self.denominator * frac.denominator
        return Fraction(num, denom)
    
    def __sub__(self, frac):
        """Return the difference of two fractions as a new fraction."""
        # avoid duplicate code, use self + (-frac)
        return self.__add__(-frac)
    
    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction."""
        num = self.numerator * frac.numerator
        denom = self.denominator * frac.denominator
        return Fraction(num, denom)
    
    def __eq__(self, frac):
        """Test if two fractions have the same value.

           Fractions are stored in proper form so the internal 
           representation is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
