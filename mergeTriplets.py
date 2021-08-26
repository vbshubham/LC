from functools import reduce
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target

        def merge(t1, t2):
            return tuple(max(a, b) for a, b in zip(t1, t2))

        try:
            m = reduce(merge, ((a, b, c) for a, b, c in triplets if a <= ta and b <= tb and c <= tc))
        except TypeError:
            return False
        return m == tuple(target)


if __name__ == '__main__':
    print(Solution().mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [0, 0, 0]))
