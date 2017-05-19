#!/usr/bin/env python
"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if m < n:
            return 0

        mat = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            mat[i][0] = 1

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    mat[i][j] = mat[i - 1][j] + mat[i - 1][j - 1]
                else:
                    mat[i][j] = mat[i - 1][j]

        return mat[-1][-1]

if __name__ == '__main__':
    so = Solution()

    print so.numDistinct('rabbbit', 'rabbit')
    print so.numDistinct('ABCDE', 'ACE')
    print so.numDistinct('ABBB', 'AB')
