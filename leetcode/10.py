#!/usr/bin/env python
"""
Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution(object):
    """
    O(n^2)
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m, n = len(p), len(s)

        table = [[False for j in xrange(n + 1)] for i in xrange(m + 1)]
        table[0][0] = True

        # assue * is zero
        for i in range(2, m + 1):
            if p[i - 1] == '*':
                table[i][0] = table[i - 2][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] != '*':
                    if p[i - 1] == '.' or p[i - 1] == s[j - 1]:
                        table[i][j] = table[i - 1][j - 1]
                else:
                    if table[i - 2][j] == True:
                        table[i][j] = True
                    else:
                        table[i][j] = table[i - 1][j]
                        
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
                        
        return table[-1][-1]
