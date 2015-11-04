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
        
        list_length = 0
        temp = head
        while temp:
            list_length += 1
            temp = temp.next
        
        if list_length == 0 or k % list_length == 0:
            return head
        else:
            k %= list_length
        
        temp1, count  = head, k
        while count:
            temp1 = temp1.next
            count -= 1
        
        temp2 = head
        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = head
        head = temp2.next
        temp2.next = None
        return head
        
        
        
        