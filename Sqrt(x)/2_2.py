class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        left, right = 0, x + 1
        while left < right:
            middle = (left + right) >> 1
            if middle * middle == x:
                return middle
            elif x > middle * middle:
                left = middle + 1
            else:
                right = middle - 1
        return (left - 1, left)[x >= left * left]