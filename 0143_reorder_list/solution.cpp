/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
typedef struct ListNode LN;

class Solution {
public:
    void reorderList(ListNode* head) {
        // find mid point of list
        LN *slow = head;
        LN *fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse 2nd half
        LN *prev = nullptr;
        LN *head2 = slow->next;
        LN *next;
        while (head2) {
            next = head2->next;
            head2->next = prev;
            prev = head2;
            head2 = next;
        }
        slow->next = nullptr;

        // merge lists
        LN *head1 = head;
        head2 = prev;
        while (head2 != nullptr) {
            next = head1->next;
            head1->next = head2;
            head1 = head2;
            head2 = next;
        }
    }
};