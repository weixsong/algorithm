#!/usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Time: O(n^2)
        timeout
        """
        if prices == None or len(prices) == 0:
            return 0

        profit = 0
        for i in range(len(prices)):
            p1 = self.max_p(prices, 0, i)
            p2 = self.max_p(prices, i, len(prices) - 1)
            profit = max(profit, p1 + p2)

        return profit

    def max_p(self, prices, start, end):
        if start >= end:
            return 0

        min_price = prices[start]
        profit = 0

        for i in range(start, end + 1):
            p = prices[i]
            profit = max(p - min_price, profit)
            min_price = min(min_price, p)

        return profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Time: O(n)
        Space: O(n)
        """
        
        if prices == None or len(prices) < 2:
            return 0

        max_profit = [0 for p in prices]
        min_price = prices[0]

        for i in range(1, len(prices)):
            p = prices[i]
            max_profit[i] = max(max_profit[i - 1], p - min_price)
            min_price = min(min_price, p)

        max_price = prices[-1]
        profit = 0
        for i in range(len(prices) - 2, -1, -1):
            p = prices[i]
            profit = max(max_price - p + max_profit[i], profit)
            max_price = max(p, max_price)

        return profit

if __name__ == '__main__':
    so = Solution()

    print so.maxProfit([2,1,2,0,1])
