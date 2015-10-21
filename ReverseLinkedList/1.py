# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        else:
            a = head
            b = head.next
            
            if b.next == None:
                b.next = a
                a.next = None
                return b
            else:
                a.next = None
            while b.next != None:
                c = b.next
                b.next = a
                a = b
                b = c
            b.next = a
            return b