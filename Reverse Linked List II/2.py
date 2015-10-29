class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None or m==n:
            return head
        start = ListNode(-1)
        start.next = head
        
        first, second = start, head
        i = 1
        while second != None:
            if i == m:
                break
            else:
                i += 1
                first = first.next
                second = second.next
        minus = n - m
        third, fourth = second, second.next
        temp = None
        while minus != 0:
            minus -= 1
            temp = fourth.next
            fourth.next = third
            third = fourth
            fourth = temp
        second.next = fourth
        first.next = third
        return start.next