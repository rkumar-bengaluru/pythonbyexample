import unittest

from turing.number_generator import NumberGenerator

class NumberGeneratorTest(unittest.TestCase):

    def test_generate_number(self):
        digits = [0, 1, 2, 3, 4, 5, 6,7, 8, 9]
        num = 210
        sol = NumberGenerator()
        time = sol.generate_number(digits=digits, num=num)
        self.assertEqual(time, 4)

    def test1_generate_number(self):
        digits = [8, 4, 5, 9, 7, 6, 1, 2, 0, 3]
        num = 5439
        sol = NumberGenerator()
        time = sol.generate_number(digits=digits, num=num)
        self.assertEqual(time, 17)

    # def test2_generate_number(self):
    #     digits = "0123456789"
    #     num = "5439"
    #     sol = NumberGenerator()
    #     time = sol.number_generate(digits=digits, nums=num)
    #     self.assertEqual(time, 13)