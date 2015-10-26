class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        headA_length = self.getLength(headA)
        headB_length = self.getLength(headB)
        if headA_length == 0 or headB_length == 0:
            return None
        else:
            length_min = min(headA_length, headB_length)
            while headA_length > length_min:
                headA_length -= 1
                headA = headA.next
            while headB_length > length_min:
                headB_length -= 1
                headB = headB.next
            while headA:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None
            
            
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length