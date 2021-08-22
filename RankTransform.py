from heapq import heapify, heappop
from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        inf = 10 ** 10
        pq = [(elem, i, j) for i, row in enumerate(matrix) for j, elem in enumerate(row)]
        heapify(pq)
        row = [(0, -inf)] * m
        col = [(0, -inf)] * n
        while pq:
            cur, r, c = heappop(pq)
            