from typing import List


def reverse_index(ls, elem):
    for i in range(len(ls)-1, -1, -1):
        if ls[i] == elem:
            return i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i, j = 0, len(sorted_nums) - 1
        while i < j:
            if sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            elif sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            else:
                return [nums.index(sorted_nums[i]), reverse_index(nums, sorted_nums[j])]
