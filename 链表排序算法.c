/***
题目描述：  针对单项链表，利用快速排序的思想对链表排序

solution：
快排的思路是： 找到数组的一个数组，然后两个首尾指针，找到前面都比当前数字大，后面都比当前数字小；
	       然鹅，单链表是没办法从尾指针向前遍历的，怎么办呢？
 	       可以利用前后指针，前指针永远指向比key小的最后一个数字，后指针遍历链表；遇到比key小的，就交换pre的next节点的值跟后指针值
***/

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
    ListNode* sortList(ListNode* head) {
        
        ListNode* p_end = NULL;
        if (head != p_end) {
            
            ListNode* par = quickSort(head, p_end);
            quickSort(head, par);
            quickSort(par->next, p_end);
        }
        
        return head;
    }

public:
    ListNode* quickSort(ListNode* head, ListNode* tial){
        
        if (head == NULL || head == tial) return head;
        
        int key = head->val;
        ListNode* p = head;
        ListNode* q = head->next;
        
        while(q != NULL) {
            if (q->val < key) {
                p = p->next;
                int temp = q->val;
                q->val = p->val;
                p->val = temp;
            }
            q = q->next;
        }
        
        head->val = p->val;
        p->val = key;
        return p;
    }
};
