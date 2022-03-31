class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        profit = 0
        n=len(prices)
        for i in range(1, n):
            diff = prices[i] - buy
            buy = min(buy, prices[i])
            profit = max(profit, diff)
        return profit