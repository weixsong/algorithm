# -*- encoding: utf-8 -*-
'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

class Solution(object):
    '''
    O(n)
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for num in nums:
            if num == target:
                return True

        return False

class Solution(object):
    '''
    O(logn), binary search
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                return self.line_search(left, right, nums, target)

            if nums[mid] == target:
                return True

            if nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

    def line_search(self, left, right, nums, target):
        for i in range(left, right + 1):
            if nums[i] == target:
                return True

        return False