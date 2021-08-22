from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [(-(stones // 2), stones) for stones in piles]
        heapify(pq)
        for _ in range(k):
            to_rem, cur = heappop(pq)
            rem = cur + to_rem
            if rem > 0:
                heappush(pq, (-(rem // 2), rem))
        return sum(stones for _, stones in pq)


if __name__ == '__main__':
    print(Solution().minStoneSum([5, 4, 9], 2))
