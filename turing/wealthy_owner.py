from typing import List

class WealthyOwners:

    def find_wealthy_owner(self, lockers: List[int]):
        """
        You are given 2D matrix where lockers[m][n] represents the value of lockers. Provided the net
        worth of the wealthiest owner, calculate the sum total of the value they posses in all their lockers

        Args:
            lockers (List<int>): lockers of all owners

        Returns:
            int: worth of wealthy owner
        """
        wealths = []
        for owner in lockers:
            wealths.append(sum(owner))
        wealths = sorted(wealths)

        return wealths[-1]