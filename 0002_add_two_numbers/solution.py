from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# helper function for Solution1
def calculate(n1: int, n2: int, quotient: int) -> Tuple[int, int]:
    _sum: int = n1 + n2 + quotient
    quotient = _sum // 10
    n2 = _sum % 10
    return quotient, n2

# beats 20% runtime, 85% memory 
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head: Optional[ListNode] = ListNode()
        curr: Optional[ListNode] = head
        curr1: Optional[ListNode] = l1
        curr2: Optional[ListNode] = l2
        quotient: int = 0
        new_val: int = 0
        while curr1 or curr2:
            node: Optional[ListNode] = ListNode()
            if curr1 and curr2:
                quotient, new_val = calculate(curr1.val, curr2.val, quotient)
                curr1 = curr1.next
                curr2 = curr2.next
            elif not curr1:
                quotient, new_val = calculate(0, curr2.val, quotient)
                curr2 = curr2.next
            elif not curr2:
                quotient, new_val = calculate(curr1.val, 0, quotient)
                curr1 = curr1.next
            node.val = new_val
            curr.next = node
            curr = curr.next
        if quotient > 0:
            curr.next = ListNode(quotient)
        return head.next

# beats 72.85% runtime, 57.20% memory 
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head: Optional[ListNode] = ListNode()
        curr: Optional[ListNode] = head

        _sum: int = 0
        quotient: int = 0
        while l1 or l2 or quotient:
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0
            
            _sum = val1 + val2 + quotient
            quotient = _sum // 10
            curr.next = ListNode(_sum % 10)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next

        