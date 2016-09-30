struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL) return l2;
        if (l2 == NULL) return l1;

        ListNode *head = new ListNode(0);
        int carrier = 0;
        ListNode *p = head;

        while (l1 != NULL && l2 != NULL)
        {
            int val = l1->val + l2->val + carrier;
            carrier = val / 10;
            val %= 10;

            p->next = new ListNode(val);
            p = p->next;

            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1 != NULL)
        {
            int val = l1->val + carrier;
            carrier = val / 10;
            val %= 10;

            p->next = new ListNode(val);
            p = p->next;

            l1 = l1->next;
        }

        while (l2 != NULL)
        {
            int val = l2->val + carrier;
            carrier = val / 10;
            val %= 10;
            
            p->next = new ListNode(val);
            p = p->next;

            l2 = l2->next;
        }

        if (carrier != 0)
        {
            p->next = new ListNode(carrier);
        }

        return head->next;
    }
};