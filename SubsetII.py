from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(1 << n):
            res.add(sorted(nums[j] for j in range(n) if i & (1 << j)))
        return [list(tup) for tup in res]
