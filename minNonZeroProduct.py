import operator
from functools import reduce


def neighs(cur):
    n = cur
    for i in range(n):
        if


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        arr = tuple(range(2, 2 ** p))
        q = [arr]
        seen = {arr}
        res = reduce(operator.mul, arr, 1)
        while q:
            cur = q.pop()
            cur_pro = reduce(operator.mul, cur,1)
            if cur_pro < res:
                print(cur)
                res = cur_pro
            for nr in neighs(cur):
                if nr not in seen:
                    q.append(nr)
                    seen.add(nr)
        return res