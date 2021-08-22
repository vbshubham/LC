from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones = [-i for i in milestones]
        heapify(milestones)
        res = 0
        while len(milestones) > 1:
            a, b = -heappop(milestones), -heappop(milestones)
            res += 2 * b
            if a > b:
                heappush(milestones, b - a)
        if milestones:
            res += 1
        return res


if __name__ == '__main__':
    # print(Solution().numberOfWeeks([1, 2, 3]))
    print(Solution().numberOfWeeks([5,7,5,7,9,7]))
