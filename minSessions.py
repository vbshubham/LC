from functools import lru_cache
from typing import List


def not_in(mask, tasks):
    for j in range(len(tasks)):
        if mask & (1 << j) == 0:
            yield tasks[j]


def valid(mask, tasks, sessionTime):
    res = sum(tasks[j] for j in range(len(tasks)) if mask & (1<<j) != 0)
    return res <= sessionTime


class Solution:
    def minSessions(self, tasks_list: List[int], sessionTime: int) -> int:
        @lru_cache(None)
        def f(tasks):
            n = len(tasks)
            if n == 0:
                return 0
            res = min((f(tuple(sorted(not_in(i, tasks)))) + 1 for i in range(1, 1<<n)
                       if valid(i, tasks, sessionTime)))
            return res
        return f(tuple(sorted(tasks_list)))


if __name__ == '__main__':
    print(Solution().minSessions([1,2,3], 3))
