# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None or m==n:
            return head
        start = ListNode(-1)
        start.next = head
        temp = start
        temp2 = head
        i = m
        i -= 1
        while i:
            i -=1
            temp = temp.next
            temp2 = temp2.next
        beforestart= temp
        startofreverse = temp2
        temp = temp2
        temp2 = temp2.next
        minus = n - m
        while minus:
            minus -= 1
            temp3 = temp2.next
            temp2.next = temp
            temp = temp2
            temp2 = temp3
        startofreverse.next = temp2
        if m == 1:
            return temp
        else:
            beforestart.next = temp
            return head
        