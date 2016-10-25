#!/usr/bin/env python

"""
Reverse Integer
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        int_max = 2147483647 / 10

        negative = False
        if x < 0:
            negative = True
            x = -x

        reversed = 0
        while x != 0:
            if reversed > int_max:
                # overflow
                return 0

            reminder = x % 10
            x = x / 10
            reversed = reversed * 10 + reminder

        if negative:
            reversed = -reversed

        return reversed

