from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        neg = []
        abs_sum = 0
        for row in matrix:
            for elem in row:
                if elem < 0:
                    neg.append(elem)
                abs_sum += abs(elem)
        if len(neg) % 2 == 0:
            return abs_sum
        else:
            return abs_sum - 2 * min(abs(elem) for row in matrix for elem in row)
