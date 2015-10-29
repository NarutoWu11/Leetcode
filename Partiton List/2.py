class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head or head.next == None:
            return head
        
        start = ListNode(-1)
        start.next = head
        
        start_bigger = ListNode(x)
        
        temp_first, temp_second = start, head
        temp_bigger = start_bigger
        while temp_second != None:
            if temp_second.val < x:
                temp_first = temp_first.next
                temp_second = temp_second.next
            else:
                temp_first.next = temp_second.next
                temp_second.next = None
                temp_bigger.next = temp_second
                temp_bigger = temp_bigger.next
                temp_second = temp_first.next
                
        temp_first.next = start_bigger.next
        
        return start.next