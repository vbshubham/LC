from typing import List


def checkdir(r, c, color, board, dr, dc):
    m, n = len(board), len(board[0])
    r += dr
    c += dc
    cnt = 0
    while 0 <= r < m and 0 <= c < n:
        if board[r][c] == '.':
            return False
        if board[r][c] == color:
            return cnt >= 1
        cnt += 1
        r += dr
        c += dc
    return False


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        return any(checkdir(rMove, cMove, color, board, dr, dc) for dr, dc in dirs)


if __name__ == '__main__':
    print(Solution().checkMove([[".", ".", "W", ".", "B", "W", "W", "B"],
                                ["B", "W", ".", "W", ".", "W", "B", "B"],
                                [".", "W", "B", "W", "W", ".", "W", "W"],
                                ["W", "W", ".", "W", ".", ".", "B", "B"],
                                ["B", "W", "B", "B", "W", "W", "B", "."],
                                ["W", ".", "W", ".", ".", "B", "W", "W"],
                                ["B", ".", "B", "B", ".", ".", "B", "B"],
                                [".", "W", ".", "W", ".", "W", ".", "W"]]
                               , 5, 4
                               , "W"))
