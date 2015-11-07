/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode LS, *PLS; 

void reorderList(struct ListNode *head) {
   if ((head == NULL)||(head->next == NULL))    return;
   PLS a = head, b = head->next;
   //find the middle node
   while((b!=NULL)&&(b->next!=NULL))
   {
       a = a->next;
       b = b->next->next;
   }
   
   //after the while loop, a->next is the middle node
   //i is j's previous node
   //reverse the second half
   PLS sechead = a->next, i = a->next, j = a->next->next, temp = NULL, temp2 = NULL;
   a->next = NULL;
   while (j!=NULL)
   {
       temp = j->next;
       j->next = i;
       i = j;
       j = temp;
   }
   sechead ->next = NULL;
   sechead = i;
   
   i = head, j = sechead;
   while (i->next != NULL)
   {
       temp = i->next;
       temp2 = j->next;
       i->next = j;
       j -> next = temp;
       i = temp; 
       j = temp2;
   }
   if (j!=NULL)
   {
       i ->next = j;
   }
   
   
}