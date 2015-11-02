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
            while temp2 and temp2.next:
                if temp2.next.val == temp2.val:
                    temp2 = temp2.next
                    while temp2.next:
                        if temp2.next.val == temp2.val:
                            temp2 = temp2.next
                        else:
                            break
                    temp.next = temp2.next
                    temp2 = temp.next
                else:
                    temp = temp2
                    temp2 = temp2.next
                    
            return start.next