class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(0, len(A)):
        	if A[i] == target:
        		return i
        	elif A[i] > target:
        		return i
        	else:
        		continue
       	return len(A)