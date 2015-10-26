# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   The main idea of this solution is using the values of the intersecting nodes.
#   First, calculate the total amount of value of nodes in listB.
#   Second, add 1 to all the nodes in listA.
#   Third, re-calculate the total amount of value in listB.
#   If there exists some nodes intersecting, the re-calculated amount must be different from the previous one,
#   otherwise, there is no any node intersecting. 
#   And we can also derive the first intersecting node through the difference between two amounts.

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        totalA = 0
        totalA2rd = 0
        pA, pB= headA, headB
        lengthB = 0

        
        while pA:
            totalA += pA.val
            pA = pA.next
        while pB:
            lengthB += 1
            pB.val +=1
            pB = pB.next
        pA = headA
        while pA:
            totalA2rd += pA.val
            pA = pA.next
        if totalA == totalA2rd:
            pB = headB
            while pB:
                pB.val -=1
                pB = pB.next
            return None
        else:
            minus = lengthB - (totalA2rd - totalA)
            pB = headB
            while minus:
                pB = pB.next
                minus -= 1
            #let headB be the original one
            pB2 = headB
            while pB2:
                pB2.val -=1
                pB2 = pB2.next
            return pB