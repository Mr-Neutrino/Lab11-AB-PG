# https://github.com/Mr-Neutrino/Lab11-AB-PG
# Partner 1: Alessandro Barbieri
# Partner 2: Prabhav Govindu

from unittest import TestCase
from calculator import *

class TestCalculator(TestCase):
    def test_multiply(self):
        self.assertEqual(mul(5, 2), 10)

    def test_divide(self):
        self.assertEqual(div(10, 5), 2)

    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm(-1, 5))

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(4), 2)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(4, 2), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0, 10)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 4), 2)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 0, 0)

