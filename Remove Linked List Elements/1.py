# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head == None:
            return head
            
        # consider if head.val == val or the middle node's val == val
        while head and head.val == val:
            head = head.next
        start = head
        while start and start.next :
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next
        return head
        