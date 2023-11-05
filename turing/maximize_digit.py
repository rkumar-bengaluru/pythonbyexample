import string

class MaximizeDigit:

    def find_max(self, k: int) -> int:

        """
        Given a number x your goal is to generate the largest number using the digits of x, you are allowed to switch
        one digit with another one in x

        Args:
            k (int):    input number
        Return:
            int:    output
        """
        s = list(str(k))
        num_map = { c: i for i , c in enumerate(s)}
        print(num_map)

        for i, c in enumerate(s): # 0, 1
            for digit in reversed(string.digits): 
                if digit <= c:
                    break
                if digit in num_map and num_map[digit] > i:
                    s[i], s[num_map[digit]] = digit, s[i]
                    return int(''.join(s))

        return k