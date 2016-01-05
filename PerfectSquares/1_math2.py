class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n >>= 2
        
        if n % 8 == 7:
            return 4
        else:
            sqrt_n = int(math.sqrt(n))
            if sqrt_n * sqrt_n == n:
                return 1
            else:
                for i in xrange(1, sqrt_n + 1):
                    sqrt_remain = int(math.sqrt( n - i * i))
                    if sqrt_remain*sqrt_remain == n - i*i:
                        return 2
                return 3
                    
                
        