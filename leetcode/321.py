#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

'''

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        m, n = len(nums1), len(nums2)
        ans = [0] * k

        min_k = max(0, k - n)
        max_k = min(m, k)

        for i in range(min_k, max_k + 1):
            res1 = self.find_max(nums1, i)
            res2 = self.find_max(nums2, k - i)
            cand = self.merge(res1, res2)
            if self.greater(cand, ans, 0, 0):
                ans = cand

        return ans

    def find_max(self, nums, k):
        res = []
        for i in range(len(nums)):
            while len(res) > 0 and len(res) + len(nums) - i > k and nums[i] > res[-1]:
                res.pop()

            if len(res) < k:
                res.append(nums[i])

        return res

    def merge(self, nums1, nums2):
        res = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if self.greater(nums1, nums2, i, j):
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res


    def greater(self, nums1, nums2, i, j):
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            i += 1
            j += 1

        return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])






