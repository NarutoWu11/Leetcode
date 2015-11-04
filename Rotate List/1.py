# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = ListNode(0)
        
        count = 0
        temp = head
        temp2 = head
        
        # count the number of nodes
        while temp:
            temp2 = temp
            temp = temp.next
            count += 1
            
        # consider 2 situation
        if count == 0:
            return head
        k %= count
        if k == 0:
            return head
        
        #rotate
        minus = count - k
        temp2.next = head
        start.next= head
        temp = head
        temp2 = start
        while minus:
            temp = temp.next
            temp2 = temp2.next
            minus -= 1
        start.next = temp
        
        temp2.next = None
        return start.next