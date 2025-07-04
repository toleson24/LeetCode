from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# runtime: 100%, space: 91.27%
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        left: bool = self.isSameTree(p.left, q.left)
        right: bool = self.isSameTree(p.right, q.right)

        return left and right
        
        