class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:        	
        	return l2
        elif l2 is None:
        	return l1
        else:
        	if l1.val > l2.val:
        		l3 = ListNode(l2.val)
        		l2 = l2.next
        		l3head = l3
        	else:
        		l3 = ListNode(l1.val)
        		l1 = l1.next
        		l3head = l3
        	while l2 or l1:
        		if l1 is None:
        			new = l2
        			l3.next = new
        			break
        		elif l2 is None:
        			new = l1
        			l3.next = new
        			break
        		elif l1.val < l2.val:
        			new = ListNode(l1.val)
        			l1 = l1.next
        			l3.next = new
        			l3 = l3.next
        		else:
        			new = ListNode(l2.val)
        			l3.next = new
        			l3 = l3.next
        			l2 = l2.next
        	return l3head

if __name__ == "__main__":
	a = Solution()
	l1 = ListNode(5)
	l2 = ListNode(1)
	new = ListNode(2)
	new2 = ListNode(4)
	l2.next = new
	new.next = new2

	print a.mergeTwoLists(l1,l2).val
