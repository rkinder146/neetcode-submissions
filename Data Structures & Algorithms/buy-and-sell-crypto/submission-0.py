class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffixMax=[0]*len(prices)
        suffixMax[len(prices)-1] = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], prices[i])
        profit = 0
        for s, p in zip(suffixMax, prices):
            if s-p > profit:
                profit = s-p
        return profit
