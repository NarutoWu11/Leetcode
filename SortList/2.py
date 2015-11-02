# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        #must considering the end situation, so fast should be head.next
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        left, right = head, slow.next
        slow.next = None
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left,right)
        
    def merge(self, left,right):
        if not left or not right:
            return left or right
        start = ListNode(min(left.val, right.val)-1)
        temp = start
        while left or right:
            # left is None or right is None
            if not left or not right:
                temp.next = (left or right)
                break
            # none of left or right is None
            if left.val < right.val:
                temp.next = left
                temp = temp.next
                left = left.next
            else:
                temp.next = right
                temp = temp.next
                right = right.next
        return start.next
        