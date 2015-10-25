# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

if __name__ == "__main__":
	a = Solution()
	b = ListNode(1)
	c = ListNode(1)
	b.next = c

	print a.deleteDuplicates(b)