# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        else:
            fast, slow = head, head
            while slow.next is not None and fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            fast = slow.next
            slow.next = None
            slow = head
            slow = self.sortList(slow)
            fast = self.sortList(fast)
            return self.merge(fast, slow)
        
    def merge(self, fast, slow):
        if fast is None:
            return slow
        if slow is None:
            return fast
        if fast.val > slow.val:
            begin = slow
            slow = slow.next
        else:
            begin = fast
            fast = fast.next
        mergepoint = begin
        while fast is not None and slow is not None:
            if fast.val > slow.val:
                mergepoint.next = slow
                slow = slow.next
            else:
                mergepoint.next = fast
                fast = fast.next
            mergepoint = mergepoint.next
        if fast is None:
            mergepoint.next = slow
        elif slow is None:
            mergepoint.next = fast
        return begin
            