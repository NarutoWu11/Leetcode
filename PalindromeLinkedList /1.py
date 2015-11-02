# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        #typical way to find the middle node, must remember!
        #there are n nodes, if n is even: after while, slow is at the n/2+1 node
        #if n is odd: after while, slow is at the n/2+1 node
        if head == None:
            return True
        fast = slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        first = slow
        sec = slow.next
        while sec:
            temp=sec.next
            sec.next = first
            first = sec
            sec = temp
        slow.next = None
        tail = first
        while tail and tail.val == head.val:
            tail = tail.next
            head = head.next
        if tail == None:
            return True
        else:
            return False