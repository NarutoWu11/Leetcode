# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head == None:
            return head
        else:
            start = ListNode(head.val-1)
            start.next = head
            temp = start
            temp2 = head
            temp3 = head.next
            last_val = head.val-1
            while temp3:
                if temp2.val == temp3.val:
                    temp.next = temp3
                    temp2 = temp3
                    temp3 = temp3.next
                    last_val = temp2.val
                elif temp2.val == last_val:
                    temp.next = temp2.next
                    temp2 = temp2.next
                    temp3 = temp3.next
                else:
                    temp = temp.next
                    temp2 = temp2.next
                    temp3 = temp3.next
            if temp2.val == last_val:
                temp.next = None
            
            return start.next