import unittest

from turing.maximize_digit import MaximizeDigit

class MaximizeDigitTest(unittest.TestCase):

    def test_find_max(self):
        x = 1526
        sol = MaximizeDigit()
        result = sol.find_max(k=x)
        self.assertEqual(result, 6521)