class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        res = []
        while i >= 0 and j >= 0:
            q = sum(map(int, [num1[i], num2[j], c]))
            res.append(q % 10)
            c = q // 10
            i -= 1
            j -= 1
        while i >= 0:
            q = sum(map(int, [num1[i], c]))
            res.append(q % 10)
            c = q // 10
            i -= 1
        while j >= 0:
            q = sum(map(int, [num2[j], c]))
            res.append(q % 10)
            c = q // 10
            j -= 1
        if c:
            res.append(c)
        return ''.join(map(str, res[::-1]))


if __name__ == '__main__':
    print(Solution().addStrings('11', '123'))
