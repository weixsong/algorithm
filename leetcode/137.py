# -*- encoding: utf-8 -*-
'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0

            count[num] += 1

        for key in count:
            if count[key] != 3:
                return key

