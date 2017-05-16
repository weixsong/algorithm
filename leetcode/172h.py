# -*- encoding: utf-8 -*-
'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        zeroes = 0
        while n > 0:
            zeroes += n / 5
            n /= 5

        return zeroes
