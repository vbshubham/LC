from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        transform_rows = 0
        transform_cols = 0
        for i in range(m):
            if matrix[i][0]==0:
                transform_cols = 1
        for j in range(n):
            if matrix[0][j]==0:
                transform_rows = 1
        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                if elem == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, 0, -1):
                if 0 in [matrix[i][0], matrix[0][j]]:
                    matrix[i][j] = 0
        if transform_cols:
            for i in range(m):
                matrix[i][0] = 0
        if transform_rows:
            for j in range(n):
                matrix[0][j] = 0
        print(matrix)


# Todo: Fix the bug
if __name__ == '__main__':
    Solution().setZeroes([[1, 2, 3, 4],
                          [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]])
