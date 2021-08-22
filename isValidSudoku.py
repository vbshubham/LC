from typing import List


def has_dup(ls):
    empty = '.'
    ls = [elem for elem in ls if elem != empty]
    return len(ls) != len(set(ls))


def sq(r, c, board):
    for i in range(3):
        for j in range(3):
            yield board[r+i][c+j]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for rows in board:
            if has_dup(rows):
                return False
        for j in range(n):
            if has_dup(board[i][j] for i in range(n)):
                return False
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if has_dup(sq(i, j, board)):
                    return False
        return True
