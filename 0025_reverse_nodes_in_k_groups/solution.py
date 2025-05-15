from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# runtime: 43.97%, memory: 17.74%
class Solution:
    def reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        while curr != tail:
            next: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp: Optional[ListNode] = head
        count: int = 0
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # base case
        if count < k:
            return head

        # recursive step
        new_head: Optional[ListNode] = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)

        return new_head

        