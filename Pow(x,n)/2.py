class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1 or x in [0, 1]:
            return x
        if n == -1:
            return 1.0/x
            
        half = self.myPow(x, n/2) if n > 0 else self.myPow(x, (n+1)/2)
        
        if n % 2 == 1:
            if n > 0:
                return half * half * x
            else:
                return half * half / x
        else:
            return half* half