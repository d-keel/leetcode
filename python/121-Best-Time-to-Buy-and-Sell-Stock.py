class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        purchase: int = prices[0]
        best: int = 0

        for price in prices[1:]:
            if price < purchase:
                purchase = price
            else:
                best = max(best, price - purchase) 

        return best
