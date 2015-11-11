class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	profit = 0
    	day = len(prices)
    	if day <= 1:
    		return profit
    	else:
    		for i in range (1, day):
    			if prices[i] - prices[i-1] > 0:
    				profit += prices[i] - prices[i-1]
    		return profit