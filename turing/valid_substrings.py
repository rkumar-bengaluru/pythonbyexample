from typing import List

class ValidSubstrings:

    def find_valid_string(self, k: str) -> List[List[int]]:
        """
        Given a string k of lower case letters, the can be repeated and exist consecutively, a substring from k is
        considered valid if it contains at least three consecutive characgters.

        An example k = "abcdddeeeeaabbbcd" has 3 valid sub string they are dddd, eeee, bbb. You can identify the 
        substrings by pair of indices [index of first letter, index of second letter], the above example the 
        substring bbb is identified as [12,14]

        Return the indices of the valid substring of given k, must order the pairs by start index in ascending order.

        Args:
            k (str):    lowercase letters
        Returns:
            List[List[int]]:    pair of integers which has valid string.
        """
        
        pairs = []
        count = 1
        prev = k[0]
        previ = 0

        for i , c in enumerate(k):
            if i > 0:
                if c == prev:
                    count += 1
                    if i == len(k) - 1:
                        if count >= 3:
                            pairs.append([previ, i])
                else:
                    if count >= 3:
                        pairs.append([previ, i -1])
                    # reset
                    count = 1
                    prev = k[i]
                    previ = i
                    

        return pairs