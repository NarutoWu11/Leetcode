# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        else:
            # l1 and l2 are both not None
            carry = 0
            start = ListNode(0)
            temp = start
            
            next_carry = 0
            
            while l1 or l2:
                # didn't build a new node every time
                if l1 and l2:
                    next_carry = (l1.val + l2.val + carry) / 10
                    l1.val = (l1.val + l2.val + carry) % 10
                    temp.next = l1
                    
                    temp = temp.next
                    l1 = l1.next
                    l2 = l2.next
                    
                
                elif not l1:
                    next_carry = (l2.val + carry) / 10
                    l2.val = (l2.val + carry) % 10
                    temp.next = l2
                    
                    temp = temp.next
                    l2 = l2.next
                elif not l2:
                    next_carry = (l1.val + carry) / 10
                    l1.val = (l1.val + carry) % 10
                    temp.next = l1
                    
                    temp = temp.next
                    l1 = l1.next
                carry = next_carry
                
            temp.next = ListNode(1) if carry else None
            return start.next
            