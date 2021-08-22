from functools import lru_cache


class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def isPal(st, en):
            if st >= en:
                return True
            if s[st] == s[en]:
                return isPal(st + 1, en - 1)
            return False

        res = [0]
        for j in range(len(s)):
            if isPal(0, j):
                res.append(0)
            else:
                res.append(min(res[i] + 1 for i in range(j + 1) if isPal(i, j)))
        return res[-1]


if __name__ == '__main__':
    print(Solution().minCut("cdd"))
