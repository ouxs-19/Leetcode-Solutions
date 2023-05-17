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
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* previous = nullptr;
        ListNode* slower;

        int ret = INT_MIN;

        while (fast){
            slower = slow;
            slow = slow->next;
            fast = fast->next->next;
            slower->next = previous;
            previous = slower;
        }

        ListNode* left = previous;
        ListNode* right = slow;

        while (left){
            ret = max(ret, left->val + right-> val);
            left = left->next;
            right = right->next;
        }

        return ret;

    }
};