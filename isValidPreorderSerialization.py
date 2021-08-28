from collections import deque


class TreeNode:
    def __init__(self, v, left=None, right=None):
        self.val = v
        self.left = left
        self.right = right


def preorder(root):
    if root:
        yield root.val
        yield from preorder(root.left)
        yield from preorder(root.right)
    st = []
    if root:
        st.append(root)
    while st:
        cur = st.pop()
        yield cur.val
        if cur.right:
            st.append(cur.right)
        if cur.left:
            st.append(cur.left)


def last_3(ls):
    a, b, c = ls[-3:]
    return b == c == '#' and a != '#'


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        st = []
        for ch in preorder.split(','):
            print(st)
            st.append(ch)
            while len(st) >= 3 and last_3(st):
                [st.pop() for _ in range(3)]
                st.append('#')
        return tuple(st) == ('#',)


if __name__ == '__main__':
    print(Solution().isValidSerialization("9,#,93,#,9,9,#,#,#"))
