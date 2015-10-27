# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            start = ListNode(0)
            start.next = head
            last_loop = start
            temp = head
            while temp and temp.next:
                temp_next_next = temp.next.next
                temp_next = temp.next
                
                last_loop.next = temp_next
                temp_next.next = temp
                last_loop = temp
                temp = temp_next_next
            
            last_loop.next = temp
            return start.next
            

            