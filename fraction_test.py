import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def setUp(self):
        self.INFINITY = Fraction(1,0)
        self.NEG_INFINITY = Fraction(-1,0)

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        # We don't have any special representation for Infinity or NaN
        self.assertEqual("1/0", self.INFINITY.__str__())
        f = Fraction(0,0)
        self.assertEqual("0/0", f.__str__())
        

    # TODO Write tests for __init__, __eq__, +, *.

    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(2), Fraction(14,6) + Fraction(-1,3))
        ZERO = Fraction(0)
        f = Fraction(17, 18)
        self.assertEqual(f, f+ZERO)
        f = -f
        self.assertEqual(f, f+ZERO)

    def test_add_extended_values(self):
        # test if + works on extended values by shear luck
        NAN = Fraction(0,0)
        ZERO = Fraction(0)
        one = Fraction(3,3)
        self.assertEqual(self.INFINITY, ZERO+Fraction(20,0))
        self.assertEqual(self.INFINITY, Fraction(10)+self.INFINITY)
        self.assertEqual(self.NEG_INFINITY, Fraction(10)+self.NEG_INFINITY)
        self.assertEqual(NAN, ZERO + NAN)
        self.assertEqual(NAN, one + NAN)
        # the hard case
        self.assertEqual(NAN, NAN + self.INFINITY)
        self.assertEqual(NAN, NAN + self.NEG_INFINITY)
        self.assertEqual(NAN, self.INFINITY + self.NEG_INFINITY)

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        # various forms of extended values
        NAN = Fraction(0,0)
        ZERO = Fraction(0)
        self.assertTrue( self.INFINITY == Fraction(8,0) )
        self.assertTrue( self.NEG_INFINITY == Fraction(-9,0) )
        self.assertFalse( self.NEG_INFINITY == self.INFINITY )
        self.assertFalse( self.NEG_INFINITY == NAN )
        self.assertFalse( self.INFINITY == NAN )
        self.assertFalse( self.INFINITY == ZERO )
        self.assertFalse( f == NAN )
        self.assertFalse( ZERO == NAN )

if __name__ == '__main__':
    unittest.main(verbosity=2)
