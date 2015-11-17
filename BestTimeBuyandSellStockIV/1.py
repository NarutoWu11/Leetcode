class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
        #dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
        #= max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
        #dp[0, j] = 0; 0 transactions makes 0 profit
        #dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
        
        if not prices or k < 1:
            return 0
        else:
            # in this situation, we can use what the way 
            if k >= len(prices)/2:
                maxpro = 0
                for i in range(1, len(prices)):
                    maxpro += max((prices[i] - prices[i-1]), 0)
                return maxpro
            else:  
                # optimize the space complexity
                way = [[0] * len(prices) for i in range(2)] 
                cur, pre = 0, 0
                i = 1
                while i <= k:
                    if i % 2 == 1:
                        cur, pre = 1, 0
                    else:
                        cur, pre = 0, 1
                    temp = way[pre][0] - prices[0]
                    for j in range(1, len(prices)):
                        way[cur][j] = max(way[cur][j-1] , temp + prices[j])
                        temp = max(temp, way[pre][j] - prices[j])
                    i += 1
                
                return way[cur][len(prices)-1]