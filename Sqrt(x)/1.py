#math solution
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0
        else:
            first = 0.0
            last = 1.0
            while first != last:
                first = last
                last = (last+x/last)/2
            return int(last)