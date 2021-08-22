# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodesHelper(root, max_till_now):
    res = 0
    if root:
        if root.val <= max_till_now:
            res += 1
        new_max = max(max_till_now, root.val)
        res += goodNodesHelper(root.left, new_max) + goodNodesHelper(root.right, new_max)
    return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        inf = 10 ** 9
        return goodNodesHelper(root, root.val)
