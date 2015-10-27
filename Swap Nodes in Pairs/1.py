# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            head_next_next = head.next.next
            head_next = head.next
            
            head_next.next = head
            head.next = self.swapPairs(head_next_next)
            return head_next
            
            