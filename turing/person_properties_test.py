import unittest

from turing.person_properties import PersonProperties

class PersonPropertiesTest(unittest.TestCase):

    def test_sameProperties(self):
        k = [["male", "jake", "19"], ["female", "mully", "21"], ["female", "male", "30"]]
        a = "gender"
        b = "male"

        sol = PersonProperties()
        personWithSameProperies = sol.sameProperties(k=k, a=a, b=b)
        self.assertEqual(personWithSameProperies, 1)

    def test2_sameProperties(self):
        k = [["male", "jake", "19"], ["female", "mully", "21"], ["female", "male", "30"]]
        a = "gender"
        b = "female"

        sol = PersonProperties()
        personWithSameProperies = sol.sameProperties(k=k, a=a, b=b)
        self.assertEqual(personWithSameProperies, 2)