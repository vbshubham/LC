class Solution:
    def minSwaps(self, s: str) -> int:
        i, j = 0, len(s) - 1
        left = 0
        right = 0
        res = 0
        while i < j:
            if s[i] == '[' and s[j] == ']':
                i += 1
                j -= 1
                left += 1
                right += 1
            elif s[i] == ']' and left:
                left -= 1
                i += 1
            elif s[j] == '[' and right:
                right -= 1
                j -= 1
            elif s[i] == ']' and s[j] == ']':
                j -= 1
                right += 1
            elif s[j] == '[' and s[i] == '[':
                i += 1
                left += 1
            else:
                i += 1
                j -= 1
                left += 1
                right += 1
                res += 1
        return res


if __name__ == '__main__':
    for inp in [']]][[[',"][[]][][[][]", ]:
        print(inp, Solution().minSwaps(inp))
