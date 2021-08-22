from collections import deque


def is_valid(word):
    if not word or word.startswith('0'):
        return 0
    return 1 if 1 <= int(word) <= 26 else 0


class Solution:
    def numDecodings(self, s: str) -> int:
        res = deque([1])
        for i in range(len(s)):
            v1 = res[-1] * is_valid(s[i])
            v2 = res[-2] * is_valid(s[i-1:i+1]) if i>0 else 0
            res.append(v1+v2)
            res.popleft()
        return res[-1]



