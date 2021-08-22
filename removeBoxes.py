from collections import deque
from itertools import groupby
from typing import List, Tuple, Union


def neighs(state) -> List[Tuple[int, List]]:
    n = len(state)
    if n >= 1:
        yield state[0][1], state[1:]
        for i in range(1, n - 1):
            if state[i - 1][0] == state[i + 1][0]:
                yield state[i][1], state[:i - 2]


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        state = [(k, len(list(g))) for k, g in groupby(boxes)]
        q: deque[Union[int, List[Tuple[int, int]]]] = deque()
        q.append((0, state))    
        res = 0
        while q:
            d, cur = q.popleft()
            res = max(res, d)
            for val, nr in neighs(state):
                q.append([val + d, nr])
        return res


if __name__ == '__main__':
    print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
