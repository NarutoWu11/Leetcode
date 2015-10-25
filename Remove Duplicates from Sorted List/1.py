class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	if head is None or head.next is None :
    		return head
    	else:
    		temp = head
    		while temp and temp.next:
    			if temp.val == temp.next.val:
    				temp.next = temp.next.next
    			else:
    				temp = temp.next
    		return head