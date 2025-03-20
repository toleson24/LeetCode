import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val
    
    def __eq__(self, other):
        return self.node.val == other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head: Optional[ListNode] = ListNode()
        curr: Optional[ListNode] = head
        heap: List[HeapNode] = []

        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))
        
        while heap:
            node = heapq.heappop(heap).node
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))
            curr.next = node
            curr = curr.next

        return head.next
    
# memory limit exceeded 
class SolutionFailed:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head: Optional[ListNode] = ListNode()
        curr: Optional[ListNode] = head
        heap: List[HeapNode] = []

        for l in lists:
            node: Optional[ListNode] = l
            while node:
                heapq.heappush(heap, HeapNode(node))
                node = node.next
        
        while heap:
            curr.next = heapq.heappop(heap).node
            curr = curr.next

        return head.next

