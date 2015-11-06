import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = start = ListNode(0)
        h = []
        
        #build heap h
        h = [[i.val, i] for i in lists if i]
        
        #modify h into a heap
        heapq.heapify(h)
        
        while h:
            smallest = h[0]
            head.next = smallest[1]
            head = head.next
            
            #classify discussion if heapq has a next.
            if smallest[1].next == None:
                heapq.heappop(h)
            else:
                # this heapreplace operation is more efficient than a heappop() followed by a heappush()
                heapq.heapreplace(h, [smallest[1].next.val, smallest[1].next])
        
        return start.next
                