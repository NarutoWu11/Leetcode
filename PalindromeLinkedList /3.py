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
        
        # find the middle node of the linked list
        fast = slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half of the linked list
        first = None
        second = slow
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        # compare two of the half of the linekd list
        tail = first
        while tail:
            if tail.val == head.val:
                tail = tail.next
                head = head.next
            else:
                break
        if tail == None:
            return True
        else:
            return False