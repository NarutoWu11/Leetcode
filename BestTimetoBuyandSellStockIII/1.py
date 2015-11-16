import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit1 = 0
        total = 0
        base = 0 if len(prices) == 0 else prices[0]
        minus = -sys.maxint - 1
        
        
        for i in range(1, len(prices)):
            base = min(base, prices[i])
            profit1 = max(profit1, prices[i] - base)
            
            minus = max(minus, profit1 - prices[i])
            total = max(total, prices[i] + minus)
            
        return total