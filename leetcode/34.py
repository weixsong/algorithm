# -*- encoding: utf-8 -*-
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        res = self.bi_search(nums, target, 0, len(nums) - 1)
        return list(res)

    def bi_search(self, nums, target, left, right):
        if left > right:
            return -1, -1

        mid = left + (right - left) / 2
        if nums[mid] == target:
            l1, l2 = mid, mid
            if mid > left and nums[mid - 1] == target:
                l1, tmp = self.bi_search(nums, target, left, mid - 1)

            if l2 < right and nums[mid + 1] == target:
                tmp, l2 = self.bi_search(nums, target, mid + 1, right)

            return l1, l2

        if nums[mid] < target:
            return self.bi_search(nums, target, mid + 1, right)
        else:
            return self.bi_search(nums, target, left, mid - 1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left, right = 0, len(nums) - 1
        mid = None
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                break
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if left > right:
            return [-1, -1]

        lo, hi = mid, mid
        if lo > 0 and nums[lo - 1] == target:
            left, right = 0, lo - 1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid] == target:
                    lo = mid
                    right = mid - 1
                else:
                    left = mid + 1

        if hi < len(nums) - 1 and nums[hi + 1] == target:
            left, right = hi + 1, len(nums) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid] == target:
                    hi = mid
                    left = mid + 1
                else:
                    right = mid - 1

        return [lo, hi]


if __name__ == '__main__':

    so = Solution()

    nums = [5, 7, 7, 8, 8, 10]

    print so.searchRange(nums, 8)

