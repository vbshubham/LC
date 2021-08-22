class Solution:
    def numberOfCombinations(self, num: str) -> int:
        def helper(st, minm):
            res = 0
            if st == len(num):
                return 1
            for i in range(st + 1, len(num) + 1):
                start = num[st:i]
                # print(start)
                if start[0] != '0' and int(start) >= minm:
                    res += helper(i, int(start))
            return res

        return helper(0, 1)


if __name__ == '__main__':
    for tes in ['327',"9999999999999",
                "181599706296201533688444310698720506149731032417146774186256527047743490211586938068687937416089"]:
        print(Solution().numberOfCombinations(tes))
