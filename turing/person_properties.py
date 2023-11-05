from typing import List 

class PersonProperties:

    def sameProperties(self, a, b, k: List[int]) -> int:
        """
        Given an array k, where each k[i] = [gender_i, name_i, age_i] describes a person attribute and also given an attribute
        to match defined as key a and b

        The ith person is said to match the given attribute(key/value) if one of the following is true

        1. a == gender and b == gender_i
        2. a == name and b == name_i
        3. a == age and b == age_i

        Return the number of person that matches the given attribute

        Args:
            a (any):    any of gender, name or age
            b (any):    value of the gender, name or age
            k (List[int]):  array of person attributes
        Returns:
            int:    number of persons matching the attribute a and b
        """
        searchIndex = -1
        if a == "gender":
            searchIndex = 0
        elif a == "name":
            searchIndex = 1
        elif a == "age":
            searchIndex = 2
        
        personWithSameProperties = 0
        for person in k:
            if person[searchIndex] == b:
                personWithSameProperties += 1
        return personWithSameProperties