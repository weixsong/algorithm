#!/usr/bin/env python

"""
 Palindrome Number
 Determine whether an integer is a palindrome. Do this without extra space.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        num = 0
        origin = x
        while x != 0:
            reminder = x % 10
            x /= 10
            num = num * 10 + reminder

        if num == origin:
            return True
        else:
            return False
