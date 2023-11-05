import unittest

from turing.cards_group import EqualGroup

class EqualGroupTest(unittest.TestCase):

    def test_find_cards(self):
        cards = [3, 1, 3, 4, 3, 2]
        k = 6
        sol = EqualGroup()
        noOfMatches = sol.find_cards(k=k, cards=cards)
        self.assertEqual(noOfMatches, 2)
