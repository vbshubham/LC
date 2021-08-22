from heapq import heapify, heappush, heappop
from typing import List


def sums(mat):
    m, n = len(mat), len(mat[0])
    cur = []
    s = 0
    for i, row in enumerate(mat):
        row.sort()
        if len(row) > 1:
            heappush(cur, (row[1] - row[0], i, 0))
        s += row[0]
        print(row)
    yield s
    while cur:
        val, r, c = heappop(cur)
        if c < n - 1:
            s -= mat[r][c]
            c += 1
            if c < n - 1:
                heappush(cur, (mat[r][c + 1] - mat[r][c], r, c))
            s += mat[r][c]
            yield s


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        print([s for s in sums(mat)])
        return min(abs(s - target) for s in sums(mat))


if __name__ == '__main__':
    print(Solution().minimizeTheDifference(
        [[4, 2, 6],
         [2, 1, 8],
         [3, 9, 10],
         [7, 8, 9],
         [6, 3, 6],
         [5, 5, 10],
         [7, 1, 9],
         [3, 1, 5],
         [1, 3, 3],
         [3, 2, 8]]
        , 61
    ))
