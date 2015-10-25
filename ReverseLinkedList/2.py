# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return head
        start = ListNode(0)
        start.next = head
        
        first, second = start, head
        while second != None:
            second_ori_next = second.next
            second.next = first
            first = second
            second = second_ori_next
        head.next = None
        return first
            
        
        
        