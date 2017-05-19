# -*- encoding: utf-8 -*-
'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution(object):
    '''
    O(n) space
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        res = []
        for key in count:
            if count[key] != 2:
                res.append(key)

        return res

