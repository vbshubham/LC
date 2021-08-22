from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        right = [0]
        for h in reversed(height):
            right.append(max(right[-1], h))
        right = right[::-1]
        left = 0
        res = 0
        for i, h in enumerate(height):
            res += max(min(left, right[i + 1]) - h, 0)
            left = max(left, h)
        return res


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
