class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        def power(x, n):
            if n == 0:
                return 1
            else:
                half = power(x, n/2)
                if n % 2 == 1:
                    return half * half * x
                else:
                    return half * half
        if n >= 0:
            return power(x, n)
        else:
            return 1.0/power(x,-n)