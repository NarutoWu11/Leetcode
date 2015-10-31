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
            
        start = ListNode(0)
        start.next = head
        i, j = start, head
        while j!= None:
            if j.val == val:
                i.next = j.next
                j = j.next
            else:
                i = i.next
                j = j.next
        return start.next