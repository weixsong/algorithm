#!/usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        The natural states for this problem is the 3 possible transactions : buy, sell, rest. 
        Here rest means no transaction on that day (aka cooldown).
        Then the transaction sequences can end with any of these three states.

        buy[i] means before day i what is the maxProfit for any sequence end with buy.
        sell[i] means before day i what is the maxProfit for any sequence end with sell.
        rest[i] means before day i what is the maxProfit for any sequence end with rest.

        if you want to buy at day i, then day i - 1 must be cooldown

        buy[i]  = max(rest[i-1]-price, buy[i-1])
        sell[i] = max(buy[i-1]+price, sell[i-1])
        rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        """
        
        if prices == None or len(prices) < 2:
            return 0

        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        cooldown = [0] * n

        buy[0], sell[0], cooldown[0] = -prices[0], 0, 0

        for i in range(1, n):
            price = prices[i]
            buy[i] = max(buy[i - 1], cooldown[i - 1] - price)
            sell[i] = max(buy[i - 1] + price, sell[i - 1])
            cooldown[i] = max(sell[i - 1], buy[i - 1], cooldown[i - 1])

        return sell[-1]


