# -*- encoding: utf-8 -*-
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] = count[num] + 1

        for key in count:
            if count[key] > len(nums) / 2:
                return key
