import itertools
import random
from typing import List



def has_dup(ls):
    empty = '.'
    ls = [elem for elem in ls if elem != empty]
    return len(ls) != len(set(ls))


def sq(r, c, board):
    for i in range(3):
        for j in range(3):
            yield board[r + i][c + j]


def isValidSudoku(board: List[List[str]]) -> bool:
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


ctr = itertools.count()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        # print(next(ctr), board)
        empty = '.'
        for i in range(n):
            for j in range(n):
                if board[i][j] == empty:
                    ls = list(range(1, 10))
                    random.shuffle(ls)
                    for val in ls:
                        board[i][j] = str(val)
                        if isValidSudoku(board):
                            if self.solveSudoku(board):
                                return True
                    board[i][j] = empty
                    return False
        return True


if __name__ == '__main__':
    print(Solution().solveSudoku(
        [[".", ".", ".", ".", ".", "7", ".", ".", "9"], [".", "4", ".", ".", "8", "1", "2", ".", "."],
         [".", ".", ".", "9", ".", ".", ".", "1", "."], [".", ".", "5", "3", ".", ".", ".", "7", "2"],
         ["2", "9", "3", ".", ".", ".", ".", "5", "."], [".", ".", ".", ".", ".", "5", "3", ".", "."],
         ["8", ".", ".", ".", "2", "3", ".", ".", "."], ["7", ".", ".", ".", "5", ".", ".", "4", "."],
         ["5", "3", "1", ".", "7", ".", ".", ".", "."]]
    ))
