# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if k < 2 or head is None or head.next is None:
            return head
        else:
            start = ListNode(0)
            start.next = head
            # the function of tail is to see if it's the end of the list when seperating the group.
            tail = start
            # the function of first is to locate the first node of each group to start the reverse.
            first = head
            # pre is the node which is the tail of previos group after reversing
            pre, next_pre = start, None
            
            while True:
                count = k
                while count > 0 and tail != None:
                    tail = tail.next
                    count -=1
                if tail == None:
                    break
                next_pre = first
                second = first.next
                while first != tail:
                    temp = second.next
                    second.next = first
                    first = second
                    second = temp
                pre.next = first
                next_pre.next = second
                pre = next_pre
                first = second
                tail = next_pre
            return start.next
            
            s