# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        else:
            i = head
            j = head.next
            while i and j and j.next:
                if i != j:
                    i = i.next
                    j = j.next.next
                else:
                    return True
            return False