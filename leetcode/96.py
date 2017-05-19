# -*- encoding: utf-8 -*-
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

   '''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0 for i in range(n + 1)]
        dp[0] = 1

        for idx in range(1, n + 1):
            total = 0
            for i in range(1, idx + 1):
                total += dp[i - 1] * dp[idx - i]

            dp[idx] = total

        return dp[-1]

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0 for i in xrange(n + 1)]
        dp[0] = 1

        for idx in xrange(1, n + 1):
            total = 0
            for i in xrange(1, idx / 2 + 1):
                total += dp[i - 1] * dp[idx - i] * 2

            if idx % 2 == 1:
                total += dp[idx / 2] ** 2

            dp[idx] = total

        return dp[-1]
