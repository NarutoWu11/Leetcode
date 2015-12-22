# TLE. need to optimize.
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 4:
            return True
            
        else:
            dp = [1,1,1,1]
            for i in xrange(4, n):
                if dp[i-1] == 2 or dp[i-2] == 2 or dp[i-3] == 2:
                    dp.append(1)
                else:
                    dp.append(2)
                    
            return dp[n-1] == 1