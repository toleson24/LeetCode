from collections import deque 

# runtime: 18.36%, memory: 15.89%
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = deque([node])
        visited = {node.val: Node(node.val)}

        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                
                visited[curr.val].neighbors.append(visited[neighbor.val])

        return visited[node.val]

        