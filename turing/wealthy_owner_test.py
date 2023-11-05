import unittest

from turing.wealthy_owner import WealthyOwners

class WealthyOwnerTest(unittest.TestCase):

    def test_find_wealthy_owner(self):
        lockers = [[5, 6, 7], [3, 4, 3]]
        sol = WealthyOwners()
        worth = sol.find_wealthy_owner(lockers=lockers)
        self.assertEqual(worth, 18)
