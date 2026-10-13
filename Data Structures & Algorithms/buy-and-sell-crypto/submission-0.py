class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]
        for p in prices[1:]:
            min_p = min(p,min_p)
            profit = max(profit,p-min_p)

        return profit
