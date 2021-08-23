from typing import List


def not_intersect(inter1, inter2):
    return inter1[1] < inter2[0] or inter1[0] > inter2[1]


def merge(inter1, inter2):
    if not_intersect(inter1, inter2):
        return [inter1, inter2]
    return [(min(inter1[0], inter2[0]), max(inter1[1], inter2[1]))]


def length(ls):
    res = []
    for inter in sorted(ls):
        if not res:
            res.append(inter)
        else:
            res.extend(merge(res.pop(), inter))
    return sum(x2 - x1 for x1, x2 in res)


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        y_points = set()
        for _, y1, _, y2 in rectangles:
            y_points |= {y1, y2}
        y_points = sorted(y_points)
        area = 0
        for y1, y2 in zip(y_points, y_points[1:]):
            y = (y1 + y2) / 2
            x_points = []
            for h1, k1, h2, k2 in rectangles:
                if k1 < y < k2:
                    x_points.append((h1, h2))
            area += length(x_points) * (y2 - y1)
            area %= mod
        return area % mod


if __name__ == '__main__':
    print(Solution().rectangleArea([[0, 0, 1000000000, 1000000000]]))
