from typing import List

class EqualGroup:

    def find_cards(self, k: int, cards: List[int]) -> int:
        """
        Given a set of cards and an integer k, we need to group cards such that sum of the group is equal to k.
        You cannot use the same card in multiple group.

        Return the maximum number of equal groups that you can create from cards.

        Args:
            cards (List[int]):  list of cards
            k (int):    sum of group
        """
        cards_map = {}
        for card in cards:
            if card in cards_map:
                cards_map[card] += 1
            else:
                cards_map[card] = 1
        
        res = []
        for key in list(cards_map.keys()):
            diff = abs(k - key)
            if diff == key:
                # atleast 2 elements must be there
                if cards_map[key] >= 2:
                    res.append((key, diff))
                cards_map.pop(key)
            else:
                if diff in cards_map.keys():
                    res.append((key, diff))
                    cards_map.pop(key)
                    cards_map.pop(diff)

        print(res)
        return len(res)