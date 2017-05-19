# -*- encoding: utf-8 -*-
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        p0, pn = 0, 0
        n = len(nums) - 1
        while p0 <= n and nums[p0] != 0:
            p0 += 1

        pn = p0 + 1

        while pn <= n:
            if nums[pn] == 0:
                pn += 1
                continue

            nums[p0], nums[pn] = nums[pn], nums[p0]
            p0 += 1
            pn += 1
        