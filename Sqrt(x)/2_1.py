class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        left, right = 0, x + 1
        while left < right:
            middle = (left + right) >> 1
            if middle * middle <= x < (middle+1) *(middle+1):
                return middle
            elif x >= (middle+1) *(middle+1):
                left = middle + 1
            else:
                right = middle - 1
        return left