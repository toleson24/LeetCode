# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: empty list
        if not head:
            return None  # ListNode()

        head = reverseListRecursive(head)

        return head

def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    # base case: last node
    if not head.next:
        return head

    # recursive step
    new_head = reverseListRecursive(head.next)

    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = head
    head.next = None

    return new_head

        