# -*- encoding: utf-8 -*-
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class Solution(object):
    '''
    dynamic programming
    f(i) = f(i - 1) + f(i - 2)

    f(i) = f(i - 2) if s[i] == '0'

    take care of corner case: s[i] = '0'

    really interesting DP algorithm
    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0 or s[0] == '0':
            return 0

        r2, r1 = 1, 1
        for i in range(1, len(s)):
            # zero voids ways of the last because zero cannot be used separately
            if s[i] == '0':
                r1 = 0

            # possible two-digit letter, so new r1 is sum of both while new r2 is the old r1
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                temp = r1
                r1 = r2 + r1
                r2 = temp

            # one-digit letter, no new way added
            else:
                r2 = r1

        return r1

