from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# linear space
class OriginalSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        curr = head
        i = 0
        while curr and curr.next:
            if curr in nodes and nodes.index(curr) < i:
                return True
            nodes.append(curr)
            curr = curr.next
            i += 1
        return False

# constant space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        