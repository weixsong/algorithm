#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        binary search
        O(nlogn)
        """

        n = len(nums)
        left, right = 1, n - 1

        while left <= right:
            mid = left + (right - left) / 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1

        return left






