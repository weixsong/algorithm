#!/usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Idea: dynamic programming
        dp(i): the profit of day i,
        dp(i) = prices[i] - min_price or max_profit in day i - 1

        min_price: current min price till day i

        Dynamic programming equation:

        dp(i) = max | prices[i] - min_price
                    | 
                    | dp[i - 1]

        min_price = min | min_price
                        | prices[i]

        Time: O(n)
        Space: O(1)
        """
        
        if prices == None or len(prices) == 0:
            return 0

        min_price = prices[0]
        profit = 0

        for p in prices:
            profit = max(p - min_price, profit)
            min_price = min(min_price, p)

        return profit
