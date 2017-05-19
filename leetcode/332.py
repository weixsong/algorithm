#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if coins == None or len(coins) == 0 or amount == None or amount < 0:
            return -1

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for money in range(1, amount + 1):
            for coin in coins:
                if coin > money:
                    continue

                temp = dp[money - coin] + 1
                if temp < dp[money]:
                    dp[money] = temp

        return dp[-1] if dp[-1] != amount + 1 else -1

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if coins == None or len(coins) == 0 or amount == None or amount < 0:
            return -1

        coins.sort()
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for money in range(1, amount + 1):
            for coin in coins:
                if coin > money:
                    break

                temp = dp[money - coin] + 1
                if temp < dp[money]:
                    dp[money] = temp

        return dp[-1] if dp[-1] != amount + 1 else -1

        

if __name__ == '__main__':
    so = Solution()
    print so.coinChange([1,2,5], 11)
    print so.coinChange([2], 3)
    print so.coinChange([112,149,215,496,482,436,144,397,500,189], 8480)

