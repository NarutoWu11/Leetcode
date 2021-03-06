class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        left, right = 0, x/2+1
        while (left <= right):
            middle = (left+right)/2
            result = middle * middle
            if result == x:
                return middle
            elif result > x:
                
                right = middle-1
            else:
                left = middle+1
        return right
                