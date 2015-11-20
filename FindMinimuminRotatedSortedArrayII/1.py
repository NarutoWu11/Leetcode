class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        def getMin(start, end):
            if start == end or (num[start] == num[end] and end-start==1):
                return num[end]
    
            median = (start+end)/2
            if num[median] < num[median-1]:
                return num[median]
            elif num[median] > num[end]:
                return getMin(median+1, end)
            elif num[median] == num[end]:
                return getMin(start, end-1) 
            else:
                return getMin(start, median)
        return getMin(0, len(num)-1)
        