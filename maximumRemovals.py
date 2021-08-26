from typing import List


def check(s, p, removable, k):
    removed = set(removable[:k])
    s = [s[i] for i, ch in enumerate(s) if i not in removed]
    j = 0
    for ch in p:
        while j < len(s) and s[j] != ch:
            j += 1
        if j == len(s):
            return False
        j += 1
    return True


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi) // 2
            if hi - lo == 1:
                if check(s, p, removable, hi):
                    return hi
                else:
                    return lo
            if check(s, p, removable, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
