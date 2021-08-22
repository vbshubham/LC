from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        for i, obstacle in enumerate(obstacles):
            res.append(max((res[j] for j in range(i) if obstacles[j] <= obstacle), default=0) + 1)
        return res
