/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// runtime: 100.00%, memory: 29.14% 
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL;
    struct ListNode *next;

    while (head != NULL) {
        next = head->next;
        head->next = prev;

        prev = head;
        head = next;
    }

    return prev;
}