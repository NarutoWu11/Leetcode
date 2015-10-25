# the first try is better than the second try
# 1. you only need one variable temp to do the loop;
# 2. you only need one while sentence. Even though in 2.py, the time complexity
#   is also O(n)

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