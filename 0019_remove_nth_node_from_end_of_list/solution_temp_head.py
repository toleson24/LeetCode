from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# runtime: 100.00%, memory: 12.66%
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head: Optional[ListNode] = ListNode(0, head)
        temp: Optional[ListNode] = new_head
        
        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            temp = temp.next
        
        temp.next = temp.next.next

        return new_head.next

        