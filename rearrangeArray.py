from typing import List


def check(ls):
    return all(2 * b != (a + c) for a, b, c in zip(ls, ls[1:], ls[2:]))


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == '__main__':
    print(Solution().rearrangeArray([6, 2, 0, 9, 7, 1]))
