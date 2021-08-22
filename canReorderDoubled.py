from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        ctr = Counter(arr)
        for cur in sorted(arr, key=abs):
            if ctr[cur] > 0:
                if ctr[cur * 2] == 0:
                    return False
                else:
                    ctr[cur * 2] -= 1
                    ctr[cur] -= 1
        return True


if __name__ == '__main__':
    print(Solution().canReorderDoubled([-6, -3]))
