#!/usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int

        dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
        dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
               = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))

               jj: means the buy time of ith transaction

        dp[0, j] = 0; 0 transactions makes 0 profit
        dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
        """
        
        if k <= 0 or prices == None or len(prices) < 2:
            return 0

        n = len(prices)

        # if k >= n/2, then we could make maxinum number of transaction
        # because for prices, corner case is up/down/up/down/up/down..., then it contains at most n/2 profit transactions
        if k >= n / 2:
            profit = 0
            for i in range(1, n):
                if prices[i] - prices[i - 1] > 0:
                    profit += prices[i] - prices[i - 1]

            return profit

        dp = [[0 for j in range(n)] for i in range(k + 1)]

        for i in range(1, k + 1):
            localMax = dp[i - 1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + localMax)
                localMax = max(localMax, dp[i - 1][j] - prices[j])

        return dp[-1][-1]


