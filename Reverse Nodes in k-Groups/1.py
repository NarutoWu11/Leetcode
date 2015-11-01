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
        if head == None:
            return None
        if k == 1:
            return head
        #1. know the number of node. Calculate the number of k-groups
        temp = head
        numberofNode = 0
        while temp:
            numberofNode += 1
            temp = temp.next
        numberofGroup = numberofNode / k
        
        if numberofGroup == 0:
            return head
            
        #2. reverse, in this case, k >=2, numberofGroup >=1. Which means temp != None, and temp2 !=None
        temp = numberofGroup
        lastTail = None
        newhead = head
        while temp:
            
            groupHead, groupTail, newhead = self.reversePair(newhead, k)
            
            if temp == numberofGroup:
                returnNode = groupHead
            else:
                lastTail.next = groupHead
                
            lastTail = groupTail
                
            if temp == 1:
                groupTail.next = newhead
            
            
            temp -= 1
        return returnNode
    
    def reversePair(self, head, k):
        i = k-1
        temp = head
        temp2 = head.next
        while i: 
            i -= 1
            temp3 = temp2.next
            temp2.next = temp
            temp = temp2
            temp2 = temp3
        #temp is the new linked list's head, head is the new linked list's tail, temp2 is the next group's head
        return temp, head, temp2
                
            
            