class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = [0,]
        buy = [-sys.maxint-1,]
        cool = [0,]
        for x in prices:
            new_sell = max(sell[-1], buy[-1] + x)
            new_buy = max(buy[-1], cool[-1] - x)
            new_cool = sell[-1]
            sell.append(new_sell)
            buy.append(new_buy)
            cool.append(new_cool)
        
        return sell[-1]