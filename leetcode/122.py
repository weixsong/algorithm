#!/usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Idea: if we buy stock at day i, and then if day i + 1 the stock price increase, 
            then we sell that stock and buy new one at day i + 1.
            otherwise, we don't.

        Time: O(n)
        """

        if prices == None or len(prices) == 0:
            return 0
        
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit
