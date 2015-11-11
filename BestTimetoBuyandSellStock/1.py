class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1:
            return 0
        upper = prices[length-1]
        profit = 0
        for i in range(length-2, -1, -1):
            upper = max(upper, prices[i])
            profit = max(profit, upper-prices[i])
        return profit


if __name__ =='__main__':
	a = Solution()
	A = [2,1]
	print a.maxProfit(A)

