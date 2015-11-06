# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        start = ListNode(-1)
        
        heap = [[i.val, i] for i in lists if i]
        heapq.heapify(heap)
        
        temp = start

        while heap:
            smallest = heap[0]
            temp.next = smallest[1]
            temp = temp.next
            
            if smallest[1].next:
                heapq.heapreplace(heap, [smallest[1].next.val, smallest[1].next])
            else:
                heapq.heappop(heap)
        
        return start.next        