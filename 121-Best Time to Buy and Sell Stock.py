class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxpro = 0
        if len(prices) == 0 or len(prices) == 1:
            return maxpro
        minnum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minnum:
                minnum = prices[i]
            elif (prices[i] - minnum) > maxpro:
                maxpro = prices[i] - minnum
        return maxpro
