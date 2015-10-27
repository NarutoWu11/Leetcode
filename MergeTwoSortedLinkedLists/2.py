class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        temp1, temp2, new = l1, l2, start
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        while l1:
            new.next = l1
            new = new.next
            l1 = l1.next
        while l2:
            new.next = l2
            new = new.next
            l2 = l2.next
        return start.next