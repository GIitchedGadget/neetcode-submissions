class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        maxProfit = 0
        minBuyPrice= float('inf')
        for i in range (0, length):
            profit = prices[i] - minBuyPrice
            if profit > maxProfit and profit > 0:
                maxProfit = profit
            if prices[i] < minBuyPrice:
                minBuyPrice = prices[i]
        return maxProfit

        