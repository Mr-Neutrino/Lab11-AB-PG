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