class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        i = 0
        
        if len(A) == 1:
        	return A[0]
        A = sorted(A)
        while i<(len(A)-1):        	
        	if A[i] == A[i+1]:
        		i += 2
        		continue
        	else:
        		return A[i]
        #if the only integer is the last one
        return A[len(A)-1]

if __name__ == "__main__":
    
    num = [0,1,2,3,4,5,0,1,2,3,4]
    M=Solution()
    a = M.singleNumber(num)
    
    print (a)