class Solution:
    def minTimeToType(self, word: str) -> int:
        def dist(a, b):
            v1 = ord(ch) - ord(b)
            return min((-v1)%26, v1 % 26)

        prev = 'a'
        res = 0
        for ch in word:
            res += dist(ch, prev)
            prev = ch
        return res + len(word)
