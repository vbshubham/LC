from collections import Counter, deque


def contains(container, contained):
    return all(container[x] >= contained[x] for x in contained)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wind = deque()
        res = ''
        wind_ctr = Counter()
        t_ctr = Counter(t)
        for ch in s:
            wind_ctr[ch] += 1
            wind.append(ch)
            while contains(wind_ctr, t_ctr):
                if not res or len(res) > len(wind):
                    res = ''.join(wind)
                wind_ctr[wind.popleft()] -= 1
        return res


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC"
                               , "ABC"))
