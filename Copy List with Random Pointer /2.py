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
        # hashtable key: the original linked list;
        # value: the corresponding new linked list node. 
        temp = head
        head2 = RandomListNode(temp.label)
        mapofNodes = {head: head2}
        temp2 = head2
    
        while temp.next:
            temp2.next = RandomListNode(temp.next.label)
            mapofNodes[temp.next] = temp2.next
            
            temp = temp.next
            temp2 = temp2.next
        
        temp = head
        temp2 = head2
        while temp:
            if temp.random != None:
                mapofNodes[temp].random = mapofNodes[temp.random]
            
            temp = temp.next
        
        return head2
        
        
        
        
        