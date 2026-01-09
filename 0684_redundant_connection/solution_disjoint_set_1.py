from typing import List 

# runtime: 53.87%, memory: 5.15%
class DisjointSet:
    def __init__(self, n: int):
        self.N = n
        self.size = [1] * n
        self.sets = list(range(n))

    def find(self, node: int):
        if self.sets[node] == node:
            return node
        
        self.sets[node] = self.find(self.sets[node])
        return self.sets[node]

    def union(self, node1: int, node2: int):
        node1: int = self.find(node1)
        node2: int = self.find(node2)

        if node1 == node2:
            return False
        else:
            if self.size[node1] > self.size[node2]:
                self.sets[node2] = node1
                self.size[node1] += self.size[node2]
            else:
                self.sets[node1] = node2
                self.size[node2] += self.size[node1]
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n: int = len(edges)
        ds: DisjointSet = DisjointSet(n)

        for edge in edges:
            if not ds.union(edge[0] - 1, edge[1] - 1):
                return edge
        
        return []

        