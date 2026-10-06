import unittest

from fraction import Fraction


class TestFractionMult(unittest.TestCase):
    def test_mult_fraction_by_fraction(self):
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))

    def test_mult_fraction_by_integer(self):
        self.assertEqual(Fraction(3, 5) * 2, Fraction(6, 5))

    def test_mult_result_is_reduced(self):
        self.assertEqual(Fraction(2, 9) * Fraction(3, 4), Fraction(1, 6))

    def test_mult_by_zero(self):
        self.assertEqual(Fraction(7, 11) * 0, Fraction(0, 1))

    def test_mult_raises_type_error_for_unsupported_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * "3"
