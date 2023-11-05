from typing import List
from collections import defaultdict

class NumberGenerator:

    def generate_number(self, digits: List[int], num: int) -> int:
        """
        A digit only keyboard contains all 10 digits from 0 to 9, They all exist in 1 line

        Give a string of 10 digits illustrating how the keys are positioned, to type a digit, you 
        start from the index 0 to the index of the target digit. it takes |a-b| milliseconds to
        move from a to b

        Write a function to calculate the number of milliseconds needed to type a number with one finger

        Args:
            digits (List[int]): list of integers in string
            num (int):  number to type
        Returns:
            int:    no of milliseconds to take to type the input number
        """
        digits_map = { digit: index for index, digit in enumerate(digits)}
        print(digits_map)
        num_str = list(str(num))
        current = 0
        result = 0
        for i, c in enumerate(num_str):
            # index of c
            result += abs(digits_map[int(c)] - current)
            current = digits_map[int(c)]
        return result
        
    
    def number_generate(self, digits: str, nums: str) -> int:
        digits_map = { digit: index  for index, digit in enumerate(digits)}
        print(digits_map)
        # digits_dict = defaultdict(int)
        # for idx, digit in enumerate(digits):
        #     digits_dict[idx] = digit
        # print(digits_dict)
        result = 0
        current = 0
        for digit in nums:
            time = abs(digits_map[digit] - current)
            result += time 
            current = digits_map[digit]
        print(result)
        return result