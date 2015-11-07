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
        if not l1 :
            return l2
        elif not l2:
            return l1
        else:
            head1 = l1
            head2 = l2
            head3 = ListNode(0)
            start = head3
            carry = 0
            
            while head1 or head2:
                if not head1:
                    start.next= ListNode((head2.val+carry)%10)
                    carry = (head2.val+carry)/10
                    start = start.next
                    head2 = head2.next
                    
                elif not head2:
                    start.next= ListNode((head1.val+carry)%10)
                    carry = (head1.val+carry)/10
                    start = start.next
                    head1 = head1.next
                
                else:
                    start.next= ListNode((head1.val+ head2.val +carry)%10)
                    carry = (head1.val+head2.val+carry)/10
                    start = start.next
                    head1 = head1.next
                    head2 = head2.next
            if carry:
                start.next = ListNode(carry)
            return head3.next
                    