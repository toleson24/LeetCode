from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# runtime: 100%, space: 86.76%
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        tree: List[List[int]] = []
        queue: List[TreeNode] = []  # collections.deque()
        queue.append(root)

        while queue:
            level: List[int] = []

            for _ in range(len(queue)):
                node: Optional[TreeNode] = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            tree.append(level)

        return tree

        