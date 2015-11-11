class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        base = 0 if length == 0 else prices[0]
        profit = 0
        for i in range(1, len(prices)):
            base = min(base, prices[i])
            profit = max(profit, prices[i] - base)
        return (profit, 0)[profit == 0]