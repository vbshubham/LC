class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str):
        n = len(binary)
        res = set()
        for mask in range(1, 1 << n):
            s = ''.join(binary[i] for i in range(n) if mask & (1 << i))
            # if s == '0' or not s.startswith('0'):
            res.add(s)
        return sorted(res, key=len)


def count_unique_subsequences(s):
    """Returns the number of unique subsequences of the sequence s"""
    L = {}
    N = []
    count = 1
    for c in s:
        N.append(count)
        count *= 2
        if c in L:
            count -= N[L[c] - 1]
        L[c] = len(N)
    return count - 1

# Todo:: Complete
if __name__ == '__main__':
    for st in ["101", "1010"]:
        print(Solution().numberOfUniqueGoodSubsequences(st), count_unique_subsequences(st))
