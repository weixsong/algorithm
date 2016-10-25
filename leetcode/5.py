#!/usr/bin/env python

"""
5. Longest Palindromic Substring
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""


class Solution(object):
    """
    O(n^2)
    space: O(n^2)
    Dynamic program, f(i, j) = f(i+1, j-1) + 2, if s[i] == s[j] && f(i+1, j-1) is Palindromic
    could not pass time limit!
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        mat = [[0 for j in xrange(n)] for i in xrange(n)]

        longest = ""

        for i in xrange(n):
            mat[i][i] = 1
            longest = s[i:i+1]

        for i in xrange(n - 1):
            if s[i] == s[i + 1]:
                mat[i][i + 1] = 2
                longest = s[i:i+2]

        for k in xrange(2, n):
            for i in xrange(n - k):
                j = i + k
                if mat[i+1][j-1] != 0 and s[i] == s[j]:
                    mat[i][j] = mat[i+1][j-1] + 2
                    if j - i + 1 > len(longest):
                        longest = s[i:j+1]

        return longest


class Solution(object):
    """
    O(n^2)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for i in xrange(len(s)):
            r1 = self.find(s, i, i)
            if len(r1) > len(longest):
                longest = r1

            if i < len(s) - 1 and s[i] == s[i + 1]:
                r2 = self.find(s, i, i + 1)
                if len(r2) > len(longest):
                    longest = r2

        return longest

    def find(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]


class Solution(object):
    """
    O(n^2)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        r = [1 for i in range(len(s))]
        center, max_idx = 0, 0

        for i in xrange(len(s)):
            if max_idx > i:
                sym = 2 * center - i
                if sym >= 0:
                    r[i] = min(r[sym], max_idx - i)
                else:
                    r[i] = max_idx - i

            r1 = self.find(s, i - r[i], i + r[i])
            if len(r1) > len(longest):
                longest = r1
                center = i
                max_idx = (len(longest) - 1) / 2

            if i < len(s) - 1 and s[i] == s[i + 1]:
                r2 = self.find(s, i, i + 1)
                if len(r2) > len(longest):
                    longest = r2

        return longest

    def find(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]



class Solution:
    """
    O(n)
    space: O(n)
    this solution contains some trick
    """
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if s is None or len(s) <= 1:
            return s

        longest, mid = 0, 0
        s2 = '#' + '#'.join(s) + '#'

        p = [1 for i in range(len(s2))]

        center = 0
        maxid = 0
        for i in range(len(s2)):
            if maxid > i:
                sym = 2 * center - i
                if sym >= 0:
                    p[i] = min(p[sym], maxid - i)
                else:
                    p[i] = maxid - i

            while i - p[i] >= 0 and i + p[i] < len(s2) and s2[i - p[i]] == s2[i + p[i]]:
                p[i] += 1

            if p[i] + i > maxid:
                maxid = p[i] + i
                center = i

            if p[i] > longest:
                longest = p[i]
                mid = i

        res = []
        for i in range(mid - longest + 1, mid + longest):
            if s2[i] != '#':
                res.append(s2[i])

        return ''.join(res)
