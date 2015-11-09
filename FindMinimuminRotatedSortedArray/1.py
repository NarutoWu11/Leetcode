class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        def getMin(start, end):
            if start == end:
                return num[end]
    
            median = (start+end)/2
            if num[median] < num[median-1]:
                return num[median]
            elif num[median] > num[end]:
                return getMin(median+1, end)
            else:
                return getMin(start, median-1)
        return getMin(0, len(num)-1)

if __name__ == "__main__":
    a = Solution()

    print a.findMin([1,2])