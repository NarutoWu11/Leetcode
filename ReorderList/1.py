# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast = slow = head
        
        # find the middle node of the linked list
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # find the first and second node of the second half which needs to be reversed 
        first = slow.next
        second = slow.next.next
        
        # set the tail of the first half points to None
        slow.next = None
        
        # set the tail of the reversed second half points to None
        first.next = None
        
        # need to use it in while loop
        temp = None
        
        # reverse the second half
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        
        # after reverse, the variable first is the head of second half
        # need to use it in while loop
        temp2 = None
        
        while first:
            temp = first.next
            temp2 = head.next
            
            head.next = first
            first.next = temp2
        
            first = temp
            head = temp2
        
        
        