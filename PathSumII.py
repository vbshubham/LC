from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def parentage(node, parent):
    res = []
    cur = node
    while cur:
        res.append(cur.val)
        cur = parent[cur]
    return res[::-1]


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        res = []
        q = deque()
        parent = {}
        val = {}
        if root:
            q.append(root)
            val[root] = root.val
            parent[root] = None
        while q:
            cur = q.popleft()
            if cur.left == cur.right:
                if val[cur] == target_sum:
                    res.append(parentage(cur, parent))
            for child in (cur.left, cur.right):
                if child:
                    q.append(child)
                    val[child] = child.val + val[cur]
                    parent[child] = cur
        return res


