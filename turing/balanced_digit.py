class BalancedDigit:

    def findBalancedDigit(seld, k: int) -> int:
        """
        Given a non negative integer k, find the balanced digit such that the sum of the all the integers
        between 1 to x equals the sum of all integers between x to n

        Args:
            k (int):    non negative integer between 1 to 1000
        Returns:
            int:    returns the balanced digit n or -1 if no such digit exist.
        """
        if k >=1 and k <=1000:
            for i in range(1, k+1):
                l = i
                lsum = 0
                rsum = 0
                for j in range(0, i+1):
                    lsum += j 
                for k in range(i, k+1):
                    rsum += k 
                if lsum == rsum:
                    return l 
        
        return -1