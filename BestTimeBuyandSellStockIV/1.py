class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k < 1:
            return 0
        else:
            if k >= len(prices)/2:
                maxpro = 0
                for i in range(1, len(prices)):
                    if prices[i] - prices[i-1] > 0:
                        maxpro += (prices[i] - prices[i-1])
                
                return maxpro
            else:  
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