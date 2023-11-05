import unittest

from turing.shortest_distance import ShortestDistance

class ShortestDistanceTest(unittest.TestCase):

    def test_find_manhatten_distance(self):
        x = 5
        y = 1
        locations = [[1, 1], [6, 2], [1, 5], [3, 1]]
        #              5,                      2
        sol = ShortestDistance()
        index = sol.find_manhatten_distance(x, y, locations)
        print(index)
        self.assertEqual(index, 3)