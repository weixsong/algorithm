# -*- encoding: utf-8 -*-
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution2(object):
    '''
    linear search, O(n)
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in xrange(len(nums)):
            if nums[i] == target:
                return i

        return -1

class Solution1(object):
    '''
    search both direction, actually is linear search, O(n)
    if not found in left search, then go to right half search
    worst case will lead to O(n)
    recursive
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        return self.bi_search(nums, target, left, right)

    def bi_search(self, nums, target, left, right):
        if left > right:
            return -1

        mid = left + (right - left) / 2

        if nums[mid] == target:
            return mid

        l = self.bi_search(nums, target, left, mid - 1)
        if l != -1:
            return l
        return self.bi_search(nums, target, mid + 1, right)

class Solution1(object):
    '''
    O(logn)
    recursive
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        return self.bi_search(nums, target, left, right)

    def bi_search(self, nums, target, left, right):
        if left > right:
            return -1

        mid = left + (right - left) / 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # the 1st array
            if nums[left] <= target and target < nums[mid]:
                return self.bi_search(nums, target, left, mid - 1)
            else:
                return self.bi_search(nums, target, mid + 1, right)
        else:
            # 2nd array
            if nums[mid] < target and target <= nums[right]:
                return self.bi_search(nums, target, mid + 1, right)
            else:
                return self.bi_search(nums, target, left, mid - 1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid

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

        return -1



if __name__ == '__main__':
    so = Solution()

    print so.search([4, 5, 6, 7, 0, 1, 2], 2)
    print so.search([4, 5, 6, 7, 0, 1, 2], 5)
    print so.search([4, 5, 6, 7, 0, 1, 2], 5)
    print so.search([5, 1, 3], 5)