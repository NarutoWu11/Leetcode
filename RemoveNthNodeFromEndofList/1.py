# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        #use three three pointers. a, b, tail
        #a is the b's previous pointer, tail is n ahead of b
        a, b, tail = head, head, head
        while n:
            tail = tail.next
            n -=1
        #tail已到list最末端
        if tail == None:
            return a.next
        b, tail = b.next, tail.next
        while tail != None:
            tail, a, b = tail.next, a.next, b.next
        a.next = b.next
        return head