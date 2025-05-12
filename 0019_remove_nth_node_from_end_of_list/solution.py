from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count: int = 0
        prev: ListNode = None
        curr: ListNode = head

        while curr:
            curr = curr.next
            count += 1

        if count == n:
            return head.next

        curr = head
        i: int = 0
        while i < count - n:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next

        return head

        