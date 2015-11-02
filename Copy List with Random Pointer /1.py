# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        
        temp = head
        head2 = RandomListNode(temp.label)
        temp2 = head2
        mapofNode={head: head2}
        while temp.next:
            new = RandomListNode(temp.next.label)
            temp2.next = new
            temp2 = temp2.next
            mapofNode[temp.next] = new
            temp = temp.next
        temp = head
        temp2 = head2
        while temp:
            if temp.random != None:
                temp2.random = mapofNode[temp.random]
            temp = temp.next
            temp2 = temp2.next
        return head2