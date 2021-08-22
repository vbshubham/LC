from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)
        for i in range(1 << (n - 1), 1 << n):
            if bin(i)[2:] not in nums:
                return bin(i)[2:]
        return '0' * n


if __name__ == '__main__':
    print(Solution().findDifferentBinaryString(["00", '00']))
