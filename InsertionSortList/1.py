# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        else:
            m = head
            n = head.next
            #temp = head.next
            start = ListNode(0)
            start.next = head
            while n!= None:
                if m.val <= n.val:
                    m = m.next
                    n = n.next
                else:
                    i = start
                    j = start.next
                    while j != n:
                        if j.val > n.val:
                            m.next = n.next
                            n.next = j
                            i.next = n
                            n = m.next
                            break
                        else:
                            i = i.next
                            j = j.next
                    
                    #don't change the position, stay the same, and process the next node   
                    if j == n:
                        m = n
                        n = n.next
            return start.next
            