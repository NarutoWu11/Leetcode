class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        #use three three pointers. a, b, tail
        #a is the b's previous pointer, tail is n ahead of b
        start = ListNode(0)
        start.next = head
        a = start
        b, tail = head, head
        while n:
            n -= 1
            tail = tail.next
        #means that it's the first node that should be removed
        if tail == None:
            return b.next
        else:
            while tail != None:
                a, b, tail = a.next, b.next, tail.next
            a.next = b.next
            return head