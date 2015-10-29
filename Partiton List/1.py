# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head or head.next == None:
            return head
        # find a head
        # for convenience, add an node before head, pointing to head
        
        
        start = ListNode(-1)
        start.next = head
        tempfirst = start
        tempsecond = head
        
        if head.val >= x:
            
            while tempsecond:
                if tempsecond.val < x:
                    tempfirst.next = tempsecond.next
                    tempsecond.next = head
                    head = tempsecond
                    start.next = head
                    break
                else:
                    tempfirst = tempfirst.next
                    tempsecond = tempsecond.next
        
        else:
            
            while tempsecond:
                if tempsecond.val >= x:
                    head = tempfirst
                    break
                else:
                    tempfirst = tempfirst.next
                    tempsecond = tempsecond.next
            
        if not tempsecond:
            return start.next
        else:
            tempfirst = head
            tempsecond = head.next
            while tempsecond:
                if tempsecond.val < x:
                    tempfirst.next = tempsecond.next
                    tempsecond.next = head.next
                    head.next = tempsecond
                    head = tempsecond
                    tempsecond = tempfirst.next
                else:
                    tempfirst = tempfirst.next
                    tempsecond = tempsecond.next
            return start.next