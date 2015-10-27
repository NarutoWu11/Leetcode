class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow!= fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return None
        else:
            begin = head
            while begin != slow:
                begin = begin.next
                slow = slow.next
            return begin
            