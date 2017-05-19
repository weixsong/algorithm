#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == None or len(s) == 0:
            return 0

        n = len(s)
        is_pal = [[0 for j in range(n + 1)] for i in range(n + 1)]
        dp = [i - 1 for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(i):
                if s[i - 1] == s[j] and (is_pal[j + 1][i - 1] == 1 or i - 1 - j < 2):
                    is_pal[j][i] = 1
                    if dp[j] + 1 < dp[i]:
                        dp[i] = dp[j] + 1

        return dp[-1]

if __name__ == '__main__':
    so = Solution()
    print so.minCut('aab')

    print so.minCut('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')