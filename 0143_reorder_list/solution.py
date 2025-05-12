from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow: ListNode = head
        fast: ListNode = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second: ListNode = slow.next
        slow.next = None
        node: ListNode = None

        while second:
            temp: ListNode = second.next
            second.next = node
            node = second
            second = temp

        first: ListNode = head
        second: ListNode = node

        while second:
            temp1: ListNode = first.next
            temp2: ListNode = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        