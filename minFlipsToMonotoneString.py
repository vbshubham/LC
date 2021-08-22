class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = 0
        ones = 0
        for i in map(int, s):
            if i == 1:
                ones += 1
            else:
                dp = (min(dp + 1, ones))
        return dp


if __name__ == '__main__':
    print(Solution().minFlipsMonoIncr("11011"))
