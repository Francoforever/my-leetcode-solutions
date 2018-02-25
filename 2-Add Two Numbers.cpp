/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p1=l1,* p2=l2,*preP1 = new ListNode(0);
        int flag=0;
        while(p1!=NULL&&p2!=NULL)
        {
            int addVal = p1->val + p2->val + flag;
            if(addVal > 9)
            {
                addVal -= 10;
                flag = 1;
            }else
                flag = 0;
            
            p1->val = addVal;
            preP1 = p1;
            p1 = p1->next;
            p2 = p2->next;
        }
        if(p1!=NULL || p2!=NULL)
        {
            if(p2!=NULL)
            {
                p2->val = p2->val + flag;
                preP1->next = p2;
                if(p2->val > 9)
                {
                    p2->val -= 10;
                    flag = 1;
                }else
                    flag = 0;
                preP1= p2;
                p2 = p2->next;
                while(flag&&p2!=NULL)
                {
                    p2->val = p2->val + flag;
                    if(p2->val > 9)
                        p2->val -= 10;
                    else
                        flag = 0;
                    preP1 = p2;
                    p2 = p2->next;
                }
            }else
            {
                while(flag&&p1!=NULL)
                {
                    p1->val += flag;
                    if(p1->val > 9)
                        p1->val -= 10;
                    else
                        flag = 0;
                    preP1 = p1;
                    p1 = p1->next;
                }
            }
        }
        if(flag)
        {
            ListNode* addNode = new ListNode(1);
            preP1->next = addNode;
        }
    return l1;
    }
};
