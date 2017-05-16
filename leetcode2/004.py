#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            median = (m + n) / 2 + 1
            return self.findk(nums1, 0, m - 1, nums2, 0, n - 1, median)
        else:
            median1 = (m + n) / 2
            median2 = (m + n) / 2 + 1
            a = self.findk(nums1, 0, m - 1, nums2, 0, n - 1, median1)
            b = self.findk(nums1, 0, m - 1, nums2, 0, n - 1, median2)
            return (a + b) / 2.0

    def findk(self, nums1, l1, r1, nums2, l2, r2, k):
        """find k, start from 1"""
        if r1 - l1 > r2 - l2:
            return self.findk(nums2, l2, r2, nums1, l1, r1, k)

        if l1 > r1:
            return nums2[l2 + k - 1]

        if k == 1:
            return min(nums1[l1], nums2[l2])

        pa = min(k/2, r1 - l1 + 1)
        pb = k - pa
        n1, n2 = nums1[l1 + pa - 1], nums2[l2 + pb - 1]
        if n1 > n2:
            return self.findk(nums1, l1, l1 + pa, nums2, l2 + pb, r2, k - pb)
        elif n1 < n2:
            return self.findk(nums1, l1 + pa, r1, nums2, l2, l2 + pb, k - pa)
        else:
            return n1


class Solution2(object):
    """
    O(logn)
    Binary search
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n, m = len(nums1), len(nums2)
        if (n + m) % 2 == 1:
            return self.findk(nums1, 0, n - 1, nums2, 0, m - 1, (n + m) / 2 + 1)
        else:
            a = self.findk(nums1, 0, n - 1, nums2, 0, m - 1, (n + m) / 2)
            b = self.findk(nums1, 0, n - 1, nums2, 0, m - 1, (n + m) / 2 + 1)
            return (a + b) / 2.0

    def findk(self, nums1, l1, r1, nums2, l2, r2, k):
        """
        find k-th element regard to l1/l2
        """
        if r1 - l1 > r2 - l2:
            return self.findk(nums2, l2, r2, nums1, l1, r1, k)

        if l1 > r1:
            # first array is empty
            return nums2[l2 + k - 1]

        if k == 1:
            return min(nums1[l1], nums2[l2])

        pa = min(k / 2, r1 - l1 + 1)
        pb = k - pa

        n1, n2 = nums1[l1 + pa - 1], nums2[l2 + pb - 1]
        if n1 > n2:
            return self.findk(nums1, l1, l1 + pa, nums2, l2 + pb, r2, k - pb)
        elif n1 < n2:
            return self.findk(nums1, l1 + pa, r1, nums2, l2, l2 + pb, k - pa)
        else:
            return n1


if __name__ == '__main__':
    so = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(so.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 3]
    nums2 = [2]
    print(so.findMedianSortedArrays(nums1, nums2))
