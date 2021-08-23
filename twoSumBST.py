from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root.val
        yield from inorder(root.right)


def inorder_rev(root):
    if root:
        yield from inorder_rev(root.right)
        yield root.val
        yield from inorder_rev(root.left)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = inorder(root)
        r = inorder_rev(root)
        left = next(l)
        right = next(r)
        while left < right:
            if left + right < k:
                left = next(l)
            elif left + right > k:
                right = next(r)
            else:
                return True
        return False


