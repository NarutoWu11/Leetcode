class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(n+1):
            max_sqrt = int(math.sqrt(i))
            
            if max_sqrt * max_sqrt == i:
                dp.append(max_sqrt)
            else:
                # max_sqrt * max_sqrt < i
                # To get the value of dp[n], we should choose the min
                # value from:
                #     dp[n - 1] + 1,
                #     dp[n - 4] + 1,
                #     dp[n - 9] + 1,
                #     dp[n - 16] + 1
                #     and so on...
                min_Perfect_Square = min(dp[i - j * j] for j in range(max_sqrt, 0, -1))
                dp.append(min_Perfect_Square + 1)
        return dp[n]