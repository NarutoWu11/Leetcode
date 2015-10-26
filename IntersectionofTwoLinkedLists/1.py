# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pA, pB = headA, headB
        #test len(A) add len(B)
        length = 0
        while pA:
            pA=pA.next
            length +=1
        while pB:
            pB=pB.next
            length +=1
        pA, pB = headA, headB
        while pA != pB and length >= 0:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
            length -= 1
        if length < 0:
            return None
        else:
            return pA