class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l, r = 0, 1
        while r < len(prices):
            maxprofit = max(maxprofit, prices[r] - prices[l])
            if prices[l] >= prices[r]:
                l = r
            r += 1
        return maxprofit