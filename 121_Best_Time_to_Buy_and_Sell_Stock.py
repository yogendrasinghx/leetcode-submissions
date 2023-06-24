#Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, n):
            maxPurchase = prices[i]
            profit = maxPurchase - minPurchase
            maxProfit = max(profit, maxProfit)
            minPurchase = min(minPurchase, maxPurchase)
        return maxProfit

prices = [7,3,1,5,1,3,6,4]
print(Solution().maxProfit(prices))