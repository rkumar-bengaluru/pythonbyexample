import unittest

from turing.valid_substrings import ValidSubstrings

class ValidSubstringsTest(unittest.TestCase):

    def test_find_valid_string(self):
        k = "abcdddeeeeaabbbcd"
        sol = ValidSubstrings()
        res = sol.find_valid_string(k=k)
        print("response", res)
        self.assertEqual(res, [[3, 5], [6, 9], [12, 14]])
    
    def test1_find_valid_string(self):
        k = "abcdddeeeeaabbbc"
        sol = ValidSubstrings()
        res = sol.find_valid_string(k=k)
        print("response", res)
        self.assertEqual(res, [[3, 5], [6, 9], [12, 14]])
    
    def test2_find_valid_string(self):
        k = "abcdddeeeeaabbb"
        sol = ValidSubstrings()
        res = sol.find_valid_string(k=k)
        print("response", res)
        self.assertEqual(res, [[3, 5], [6, 9], [12, 14]])
