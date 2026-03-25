from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# runtime: 100.00% memory: 52.01% 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        next = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev

        