import unittest
 
from fraction import Fraction
 
class TestFractionAdd(unittest.TestCase):

def test_add_same_denominator(self):
 self.assertEqual(Fraction(1, 5) + Fraction(2, 5), Fraction(3, 5))

def test_add_different_denominators(self):
 self.assertEqual(Fraction(1,2) + Fraction(1,3), Fraction(5,6))

def test_add_result_is_reduced(self):
 self.assertEqual(Fraction(1, 6) + Fraction(1, 3), Fraction(1, 2))

def test_add_positive_integer(self):
 self.assertEqual(Fraction(1,2)+1, Fraction(3,2))
 
def test_add_negative_integer(self):
 self.assertEqual(Fraction(1,2) - 1, Fraction(-1,2))

def test_add_integer_zero(self):
 self.assertEqual(Fraction(1,2) + 0, Fraction(1,2))

def test_add_is_commutative(self):
 a, b = Fraction(2, 7), Fraction(3, 5)
 self.assertEqual(a + b, b + a)

def test_add_returns_fraction(self):
 self.assertIsInstance(Fraction(1, 2) + Fraction(1, 3), Fraction)

def test_add_type_error(self):
 with self.assertRaises(TypeError):
  Fraction(1, 2) + "1/2"

def test_add_none_raises_type_error(self):
 with self.assertRaises(TypeError):
  Fraction(1, 2) + None

