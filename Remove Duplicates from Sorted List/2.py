# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
        ref = head
        while ref.next:
            if ref.val == ref.next.val:
                target_val = ref.val
                refed = ref.next
                while refed:
                    if refed.next == None or refed.next.val != target_val:
                        refed = refed.next
                        break
                    else:
                        refed = refed.next
                    
                ref.next = refed
            else:
                ref = ref.next
        return head