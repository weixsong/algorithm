#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    """
    Sort the array, and search from front and end
    Time: O(nlogn)
    Space: O(n)
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums = [(nums[i], i) for i in xrange(len(nums))]
        nums = sorted(nums, key=lambda x: x[0])

        front, end = 0, len(nums) - 1
        while front < end:
            x = nums[front][0] + nums[end][0]
            if x == target:
                return (nums[front][1], nums[end][1])
            elif x < target:
                front += 1
            else:
                end -= 1

        return [0, 1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    so = Solution()
    print(so.twoSum(nums, target))
