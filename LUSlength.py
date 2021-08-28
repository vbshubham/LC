from typing import List


def is_sub(st, seq):
    i = 0
    for ch in seq:
        while i < len(st) and st[i] != ch:
            i += 1
        if i == len(st):
            return False
        i += 1
    return True


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if not any(is_sub(strs[j], s) for j in range(len(strs)) if i != j):
                return len(s)
        return -1


