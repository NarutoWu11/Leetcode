# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return
        else:
            slow, fast = head.next, head.next.next
            while 1:
                if fast is None or fast.next is None:
                    return 
                elif fast == slow:
                    break
                else:
                    slow = slow.next
                    fast = fast.next.next
            begin = head
            while begin != slow:
                begin = begin.next
                slow = slow.next
            return begin
        