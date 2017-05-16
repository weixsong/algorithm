#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"

"""


class Solution(object):
    """
    Dynamic programming
    Time: O(n^2)
    Space: O(n^2)
    This will timeout
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = s[0]
        m = len(s)
        mat = [[0 for j in range(m)] for i in range(m)]

        # odd palindrome
        for i in range(m):
            mat[i][i] = 1

        # even palindrome
        for i in range(m - 1):
            if s[i] == s[i + 1]:
                mat[i][i + 1] = 2
                longest = s[i:i+2]

        # dynamic
        for k in xrange(2, m):
            for i in xrange(0, m - k):
                j = i + k
                if s[i] == s[j] and mat[i + 1][j - 1] != 0:
                    mat[i][j] = mat[i+1][j-1] + 2
                    if mat[i][j] > len(longest):
                        longest = s[i:j+1]
                else:
                    mat[i][j] = 0

        return longest


class Solution(object):
    """
    Dynamic programming
    Time: O(n^2)
    Space: O(n)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ''
        for i in range(len(s)):
            p1 = self.find(s, i, i)
            if len(p1) > len(longest):
                longest = p1

            if i < len(s) - 1 and s[i] == s[i + 1]:
                p2 = self.find(s, i, i + 1)
                if len(p2) > len(longest):
                    longest = p2

        return longest

    def find(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]


if __name__ == '__main__':
    so = Solution()
    print(so.longestPalindrome("babad"))
    print(so.longestPalindrome("aba"))
    print(so.longestPalindrome("cbbd"))
    print(so.longestPalindrome("aaaa"))
