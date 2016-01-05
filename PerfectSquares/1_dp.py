class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [sys.maxint] * (n+1)
        
        for i in range(1, n+1):
            max_sqrt = int(math.sqrt(i))
            
            if max_sqrt * max_sqrt == i:
                dp[i] = 1
            else:
                # To get the value of dp[n], we should choose the min
                # value from:
                #     dp[n - 1] + 1,
                #     dp[n - 4] + 1,
                #     dp[n - 9] + 1,
                #     dp[n - 16] + 1
                #     and so on...

                for j in range(max_sqrt, 0, -1):
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]