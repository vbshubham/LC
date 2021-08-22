from typing import List


class Solution:

    def __init__(self):
        self.res = {}

    def helper(self, piles, lo, hi):
        if lo > hi:
            return 0
        if (lo, hi) not in self.res:
            self.res[(lo, hi)] = max(piles[lo] - self.helper(piles, lo + 1, hi), piles[hi] - self.helper(piles, lo, hi - 1))
        return self.res[(lo, hi)]

    def stoneGame(self, piles: List[int]) -> bool:
        return self.helper(piles, 0, len(piles) - 1) > 0
