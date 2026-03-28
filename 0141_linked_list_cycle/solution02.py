from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# runtime: 49.23%, memory: 13.15% 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        _set = set()

        while curr and curr.next:
            if curr in _set:
                return True
            _set.add(curr)
            curr = curr.next
        
        return False

        