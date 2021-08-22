from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    if root:
        yield root
        yield from preorder(root.left)
        yield from preorder(root.right)


def node_prod(tot, s):
    return s * (tot - s)


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sub_sum = []
        mod = 10 ** 9 + 7

        def find_sum(node):
            if node:
                res = node.val + find_sum(node.left) + find_sum(node.right)
                sub_sum.append(res)
                return res
            return 0

        tot = find_sum(root)
        return max(node_prod(tot, s) for s in sub_sum) % mod
