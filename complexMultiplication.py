def real_img(num):
    r, i = num[:-1].split('+')
    return int(r), int(i)


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x1, y1 = real_img(num1)
        x2, y2 = real_img(num2)
        return f'{x1 * x2 - y1 * y2}+{x1 * y2 + y1 * x2}i'


if __name__ == '__main__':
    print(Solution().complexNumberMultiply("1+4i", "2+5i"))
