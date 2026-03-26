/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// runtime: 100.00%, memory: 12.86% 
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) 
        return head;
    
    struct ListNode *newHead = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;

    return newHead;
}