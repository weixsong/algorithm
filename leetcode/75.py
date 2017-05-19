# -*- encoding: utf-8 -*-
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] < 1:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] > 1:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

