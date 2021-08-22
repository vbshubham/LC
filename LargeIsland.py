from itertools import product, combinations
from typing import List


def val(pos, grid):
    r, c = pos
    return grid[r][c]


def neigh(pos, grid):
    r, c = pos
    m, n = len(grid), len(grid[0])
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == 1:
            yield r + dr, c + dc


def set_val(pos, val, grid):
    r, c = pos
    grid[r][c] = val


def union(u, v, parent, size):
    u, v = find(u, parent), find(v, parent)
    if u != v:
        if val(u, size) < val(v, size):
            u, v = v, u
        set_val(v, u, parent)
        set_val(u, val(v, size) + val(u, size), size)


def find(u, parent):
    while u != val(u, parent):
        u_,parent_u = val(u,parent), val(val(u,parent),parent)
        set_val(u,parent)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [[(i, j) for j in range(n)] for i in range(m)]
        sz = [[1 for j in range(n)] for i in range(m)]
        for cur in product(range(m), range(n)):
            if val(cur, grid) == 1:
                for nr in neigh(cur, grid):
                    union(cur, nr, parent, sz)
        res = 0
        for cur in product(range(m), range(n)):
            if val(cur, grid) == 0:
                for nr1, nr2 in combinations(neigh(cur, grid), 2):
                    nr1, nr2 = find(nr1, parent), find(nr2, parent)
                    if nr1 != nr2:
                        res = max(val(nr1, sz) + val(nr2, sz), res)
        return res


if __name__ == '__main__':
    print(Solution().largestIsland([[1, 1], [1, 0]]))
