import unittest

from turing.balanced_digit import BalancedDigit

class BalancedDigitTest(unittest.TestCase):

    def test_findBalancedDigit(self):
        k = 49
        sol = BalancedDigit()
        digit = sol.findBalancedDigit(k)
        self.assertEqual(35, digit)