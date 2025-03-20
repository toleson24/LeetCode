from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left: int = maxDepth(root.left)
            right: int = maxDepth(root.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1

        return maxDepth(root) != -1

        